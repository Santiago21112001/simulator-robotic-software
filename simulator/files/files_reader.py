import json


class FileManager:

    def __init__(self):
        """
        Constructor for file manager
        """
        self.file = None

    def open(self, file):
        self.file = file
        f = open(file, encoding='utf-8')
        return f.readlines()

    def save(self, file=None, content=None):
        if content is None:
            content = []
        if file is not None:
            self.file = file
        if self.file is not None:
            f = open(self.file, "w")
            f.write("%s\n" % content)


class RobotDataReader:

    def __init__(self):
        """
        Constructor for robot data reader
        """

        self.__read_files()
        #self.__read_robot_data_file()

    def __read_files(self):
        # Read robots file
        with open("robots.json", "r") as file:
            data = json.load(file)
            self.robots = data['robots']

        # Read circuits file
        with open("circuits.json", "r") as file:
            data = json.load(file)
            self.circuits = data['circuits']

    def __read_robot_data_file(self):
        with open("robot_data.json", "r") as file:
            data = json.load(file)
            self.robots = data['robots']
            self.circuits = data['circuits']

    def parse_robot(self, robot_opt):
        """
        Parses robot's configuration from json file
        Arguments:
            robot_opt: the number of the robot to load
        Returns:
            A list of tuples with the corresponding pins
        """
        list_elem = []
        robot_name = self.__name_from_opt(robot_opt)
        for robot in self.robots:
            if robot['name'] == robot_name:
                for elem in robot['elements']:
                    list_elem.append((elem['name'], elem['pin']))
        return list_elem

    def parse_circuit(self, circuit_name):
        """
        Parses circuit's straights and obstacles
        Arguments:
            circuit_name: the name of the circuit
        Returns:
            A tuple with the straights and the obstacles
        """
        circuit_parts = []
        obstacles = []
        for circuit in self.circuits:
            if circuit_name == circuit['name']:
                if 'parts' in circuit:
                    circuit_parts = circuit['parts']
                    #circuit_parts = self.__read_parts(circuit['parts'])
                if 'obstacles' in circuit:
                    obstacles = self.__read_obstacles(circuit['obstacles'])
        return circuit_parts, obstacles

    def __name_from_opt(self, robot_opt):
        """
        Gets the name given the option number
        Arguments:
            robot_opt: the number of the robot
        Returns:
            The name of the robot that has been requested
        """
        if robot_opt == 0:
            return "mobile2"
        elif robot_opt == 1:
            return "mobile3"
        elif robot_opt == 2:
            return "mobile4"
        elif robot_opt == 3:
            return "actuator"
        elif robot_opt == 4:
            return "arduinoBoard"
        return "mobile2"

    def __read_parts(self, parts):
        """
        Reads the straights from the file
        Arguments:
            parts: the straights with the orientation
            an the length
        Returns:
            A list with the straights orientation and length
        """
        circuit_parts = []
        for part in parts:
            if part['type'] == 'straight':
                circuit_parts.append(
                    {
                        'type': part['type'],
                        'anchor': part['anchor next'],
                        part['orient']: part['dist'],
                        'save': part['save anchors']
                    }
                )
            elif part['type'] == 'turn':
                circuit_parts.append(
                    {
                        'type': part['type'],
                        'starting_angle': part['starting_angle'],
                        'angle': part['angle'],
                        'bounding_len': part['bounding_len']
                    }
                )
            elif part['type'] == 'id':
                circuit_parts.append(
                    {
                        'type': part['type'],
                        'anchor': 'end',
                        'number': part['number'],
                        'dist': part['dist']
                    }
                )
        return circuit_parts

    def __read_obstacles(self, obstacles):
        """
        Reads the obstacles from the file
        Arguments:
            obstacles: a map with the obstacles, whose
            keys are x, y, width and height
        Returns:
            A list with the obstacle properties
        """
        list_obs = []
        for obs in obstacles:
            list_obs.append(
                obs
            )
        return list_obs
