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

    def __read_files(self):
        # Read robots file
        with open("robots.json", "r") as file:
            data = json.load(file)
            self.robots = data['robots']
            self.robots = self.__put_actuator_and_board_last(self.robots)

        # Read circuits file
        with open("circuits.json", "r") as file:
            data = json.load(file)
            self.circuits = data['circuits']

    def __put_actuator_and_board_last(self, robots):
        """Puts the actuator and the Arduino board at the end of the list"""
        robots2 = []
        robots_last = []

        for robot in robots:
            if robot["name"] in ["actuator", "arduinoBoard"]:
                robots_last.append(robot)
            else:
                robots2.append(robot)

        robots2.extend(robots_last)
        return robots2

    def parse_robot(self, robot_opt):
        """
        Parses robot's configuration from json file
        Arguments:
            robot_opt: the number of the robot to load
        Returns:
            A list of tuples with the corresponding pins
        """
        list_elem = []
        robot_name = self.name_from_robot_opt(robot_opt)
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
                if 'obstacles' in circuit:
                    obstacles = self.__read_obstacles(circuit['obstacles'])
        return circuit_parts, obstacles

    def name_from_robot_opt(self, robot_opt):
        """
        Gets the name given the option number
        Arguments:
            robot_opt: the number of the robot
        Returns:
            The name of the robot that has been requested
        """
        robots = self.robots
        if robot_opt < 0:
            robot_opt = 0
        elif robot_opt > len(robots)-1:
            robot_opt = len(robots)-1
        return robots[robot_opt]["name"]

    def name_from_circuit_opt(self, circuit_opt):
        """
        Gets the name given the option number
        Arguments:
            circuit_opt: the number of the circuit
        Returns:
            The name of the circuit that has been requested
        """
        circuits = self.circuits
        if circuit_opt < 0:
            circuit_opt = 0
        elif circuit_opt > len(circuits)-1:
            circuit_opt = len(circuits) - 1
        return circuits[circuit_opt]["name"]

    def get_robots_names(self):
        names = []
        for robot in self.robots:
            names.append(robot["name"])
        return names

    def get_circuits_names(self):
        names = []
        for circuit in self.circuits:
            names.append(circuit["name"])
        return names

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
