"""
This module defines the components used for both robots.
Those being: Servos, board, sensors and inputs (button and
joystick)
"""

import robot_components.boards as boards
import robot_components.elements as elements


class Robot:

    def __init__(self, board):
        self.board = board

    def get_data(self):
        pass

    def assign_pins(self):
        pass

    def parse_pin(self, pin):
        if str(pin[0]).lower() == 'a':
            return int(pin[1]) + 14
        return int(pin)

    def add_component(self, component):
        pass


class MobileRobot(Robot):

    def __init__(self, n_ligth_sens, pins):
        """
        Constructor for mobile robot
        Arguments:
            n_light_sens: the number of light sensors
            of the robot
            pins: the used pins of the board
        """
        super().__init__(boards.BQzumBT328())

        self.servo_left = elements.Servo()
        self.servo_right = elements.Servo()

        self.light_sensors = []
        i = 0
        while i < n_ligth_sens:
            self.light_sensors.append(elements.LightSensor())
            i += 1

        self.sound = elements.UltrasoundSensor()

        self.assign_pins(pins)

    def get_data(self):
        data = None
        if len(self.light_sensors) == 2:
            data = {
                "servo_left": self.servo_left.pin,
                "servo_right": self.servo_right.pin,
                "light_left": self.light_sensors[0].pin,
                "light_right": self.light_sensors[1].pin,
                "sound_trig": self.sound.pin_trig,
                "sound_echo": self.sound.pin_echo
            }
        elif len(self.light_sensors) == 3:
            data = {
                "servo_left": self.servo_left.pin,
                "servo_right": self.servo_right.pin,
                "light_mleft": self.light_sensors[0].pin,
                "light_left": self.light_sensors[1].pin,
                "light_right": self.light_sensors[2].pin,
                "sound_trig": self.sound.pin_trig,
                "sound_echo": self.sound.pin_echo
            }
        elif len(self.light_sensors) == 4:
            data = {
                "servo_left": self.servo_left.pin,
                "servo_right": self.servo_right.pin,
                "light_mleft": self.light_sensors[0].pin,
                "light_left": self.light_sensors[1].pin,
                "light_right": self.light_sensors[2].pin,
                "light_mright": self.light_sensors[3].pin,
                "sound_trig": self.sound.pin_trig,
                "sound_echo": self.sound.pin_echo
            }
        else:
            data = {
                "servo_left": self.servo_left.pin,
                "servo_right": self.servo_right.pin,
                "light_mleft": self.light_sensors[0].pin,
                "light_left": self.light_sensors[1].pin,
                "light_right": self.light_sensors[2].pin,
                "light_mright": self.light_sensors[3].pin,
                "sound_trig": self.sound.pin_trig,
                "sound_echo": self.sound.pin_echo
            }
        return data

    def assign_pins(self, pins):
        """
        Assigns the pins to the corresponding element
        Arguments:
            pins: a list of tuples with the name of the element
            and the corresponding pin
        """
        for pin in pins:
            name = pin[0]
            pin = self.parse_pin(pin[1])
            if name == "servo left":
                self.set_servo_left(pin)
            elif name == "servo right":
                self.set_servo_right(pin)
            elif name == "light 1":
                self.set_light_mleft(pin)
            elif name == "light 2":
                self.set_light_left(pin)
            elif name == "light 3":
                self.set_light_right(pin)
            elif name == "light 4":
                self.set_light_mright(pin)
            elif name == "trig":
                self.set_sound_trig(pin)
            elif name == "echo":
                self.set_sound_echo(pin)

    def set_light_sens_value(self, values):
        """
        Sets the light sensor values
        Arguments:
            values: the values to write into the sensors
        """
        for i in range(0, len(self.light_sensors)):
            self.light_sensors[i].value = values[i]

    def set_servo_left(self, pin):
        """
        Sets servo left attached to a pin and marks
        the pin as used at the board
        """
        if self.board.check_type(pin, self.servo_left.get_pin_type()):
            if self.board.attach_pin(pin, self.servo_left):
                self.servo_left.pin = pin

    def detach_servo_left(self):
        """
        Detaches left sensor from board
        """
        self.board.detach_pin(self.servo_left.pin)
        self.servo_left.pin = -1

    def set_servo_right(self, pin):
        """
        Sets servo right attached to a pin and marks
        the pin as used at the board
        """
        if self.board.check_type(pin, self.servo_right.get_pin_type()):
            if self.board.attach_pin(pin, self.servo_right):
                self.servo_right.pin = pin

    def detach_servo_right(self):
        """
        Detaches right sensor from board
        """
        self.board.detach_pin(self.servo_right.pin)
        self.servo_right.pin = -1

    def set_light_mleft(self, pin):
        """
        Sets the most left light sensor attached to a pin
        and marks the pin as used at the board
        """
        light = self.light_sensors[0]
        if self.board.check_type(pin, light.get_pin_type()):
            if self.board.attach_pin(pin, light):
                light.pin = pin

    def detach_light_mleft(self):
        """
        Detaches the most left light sensor from board
        """
        light = self.light_sensors[0]
        self.board.detach_pin(light.pin)
        light.pin = -1

    def set_light_left(self, pin):
        """
        Sets left light sensor attached to a pin
        and marks the pin as used at the board
        """
        light = self.light_sensors[0] if len(
            self.light_sensors) == 2 else self.light_sensors[1]
        if self.board.check_type(pin, light.get_pin_type()):
            if self.board.attach_pin(pin, light):
                light.pin = pin

    def detach_light_left(self):
        """
        Detaches left light sensor from board
        """
        light = self.light_sensors[0] if len(
            self.light_sensors) == 2 else self.light_sensors[1]
        self.board.detach_pin(light.pin)
        light.pin = -1

    def set_light_right(self, pin):
        """
        Sets right light sensor attached to a pin
        and marks the pin as used at the board
        """
        light = self.light_sensors[1] if len(
            self.light_sensors) == 2 else self.light_sensors[2]
        if self.board.check_type(pin, light.get_pin_type()):
            if self.board.attach_pin(pin, light):
                light.pin = pin

    def detach_light_right(self):
        """
        Detaches right light sensor from board
        """
        light = self.light_sensors[1] if len(
            self.light_sensors) == 2 else self.light_sensors[2]
        self.board.detach_pin(light.pin)
        light.pin = -1

    def set_light_mright(self, pin):
        """
        Sets the most right light sensor attached to a pin
        and marks the pin as used at the board
        """
        light = self.light_sensors[3]
        if self.board.check_type(pin, light.get_pin_type()):
            if self.board.attach_pin(pin, light):
                light.pin = pin

    def detach_light_mright(self):
        """
        Detaches the most right light sensor from board
        """
        light = self.light_sensors[3]
        self.board.detach_pin(light.pin)
        light.pin = -1

    def set_sound_trig(self, pin):
        """
        Sets sound sensor attached to a pin (trig) and marks it
        as used at the board
        """
        if self.board.check_type(pin, self.sound.get_trig_pin_type()):
            if self.board.attach_pin(pin, self.sound):
                self.sound.pin_trig = pin

    def detach_sound_trig(self):
        """
        Detaches ultrasound sensor (trig) from board
        """
        self.board.detach_pin(self.sound.pin_trig)
        self.sound.pin_trig = -1

    def set_sound_echo(self, pin):
        """
        Sets sound sensor attached to a pin (echo) and marks it
        as used at the board
        """
        if self.board.check_type(pin, self.sound.get_echo_pin_type()):
            if self.board.attach_pin(pin, self.sound):
                self.sound.pin_echo = pin

    def detach_sound_echo(self):
        """
        Detaches ultrasound sensor (echo) from board
        """
        self.board.detach_pin(self.sound.pin_echo)
        self.sound.pin_echo = -1


class LinearActuator(Robot):

    def __init__(self, pins):
        """
        Constructor for Linear Actuator
        Arguments:
            pins: the used pins of the board
        """
        super().__init__(boards.ArduinoUno())

        self.button_left = elements.Button()
        self.button_right = elements.Button()

        self.servo = elements.Servo()

        self.joystick = elements.Joystick()

        self.assign_pins(pins)

    def get_data(self):
        return {
            "button_left": self.button_left.pin,
            "button_right": self.button_right.pin,
            "servo": self.servo.pin,
            "button_joystick": self.joystick.pinb,
            "joystick_x": self.joystick.pinx,
            "joystick_y": self.joystick.piny
        }

    def assign_pins(self, pins):
        """
        Assigns the pins to the corresponding element
        Arguments:
            pins: a list of tuples with the name of the element
            and the corresponding pin
        """
        for pin in pins:
            name = pin[0]
            pin = self.parse_pin(pin[1])
            if name == "servo":
                self.set_servo(pin)
            elif name == "button joystick":
                self.set_joystick_button(pin)
            elif name == "x joystick":
                self.set_joystick_x(pin)
            elif name == "y joystick":
                self.set_joystick_y(pin)
            elif name == "button left":
                self.set_button_left(pin)
            elif name == "button right":
                self.set_button_right(pin)

    def set_button_left(self, pin):
        """
        Attaches left button to board pin
        Arguments:
            pin: the pin of the board
        """
        if self.board.check_type(pin, self.button_left.get_pin_type()):
            if self.board.attach_pin(pin, self.button_left):
                self.button_left.pin = pin

    def detach_button_left(self):
        """
        Detaches left button from board
        """
        self.board.detach_pin(self.button_left.pin)
        self.button_left.pin = -1

    def set_button_right(self, pin):
        """
        Attaches right button to board pin
        Arguments:
            pin: the pin of the board
        """
        if self.board.check_type(pin, self.button_right.get_pin_type()):
            if self.board.attach_pin(pin, self.button_right):
                self.button_right.pin = pin

    def detach_button_right(self):
        """
        Detaches right button from board
        """
        self.board.detach_pin(self.button_right.pin)
        self.button_right.pin = -1

    def set_servo(self, pin):
        """
        Attaches servo to board pin
        Arguments:
            pin: the pin of the board
        """
        if self.board.check_type(pin, self.servo.get_pin_type()):
            if self.board.attach_pin(pin, self.servo):
                self.servo.pin = pin

    def detach_servo(self):
        """
        Detaches servo from board
        """
        self.board.detach_pin(self.servo.pin)
        self.servo.pin = -1

    def set_joystick_x(self, pin):
        """
        Attaches joystick (x) to board pin
        Arguments:
            pin: the pin of the board
        """
        if self.board.check_type(pin, self.joystick.get_x_pin_type()):
            if self.board.attach_pin(pin, self.joystick):
                self.joystick.pinx = pin

    def detach_joystick_x(self):
        """
        Detaches joystick (x) from board
        """
        self.board.detach_pin(self.joystick.pinx)
        self.joystick.pinx = -1

    def set_joystick_y(self, pin):
        """
        Attaches joystick (y) to board pin
        Arguments:
            pin: the pin of the board
        """
        if self.board.check_type(pin, self.joystick.get_y_pin_type()):
            if self.board.attach_pin(pin, self.joystick):
                self.joystick.piny = pin

    def detach_joystick_y(self):
        """
        Detaches joystick (y) from board
        """
        self.board.detach_pin(self.joystick.piny)
        self.joystick.piny = -1

    def set_joystick_button(self, pin):
        """
        Attaches joystick (x) to board pin
        Arguments:
            pin: the pin of the board
        """
        if self.board.check_type(pin, self.joystick.get_button_pin_type()):
            if self.board.attach_pin(pin, self.joystick):
                self.joystick.pinb = pin

    def detach_joystick_button(self):
        """
        Detaches joystick (x) from board
        """
        self.board.detach_pin(self.joystick.pinb)
        self.joystick.pinb = -1


class ArduinoBoard(Robot):

    def __init__(self, pins):
        """
        Constructor for arduino board
        """
        super().__init__(boards.ArduinoUno())
        self.robot_elements = []

    def add_component(self, component):
        if component == "resistance":
            resistance = elements.ResistanceArduino()
            self.robot_elements.append(resistance)
        elif component == "button":
            button = elements.ButtonArduino()
            self.robot_elements.append(button)
        elif component == "potentiometer":
            potentiometer = elements.PotentiometerArduino()
            self.robot_elements.append(potentiometer)
        elif component == "led":
            led = elements.LedArduino()
            led.set_color(1)
            self.robot_elements.append(led)
        elif component == "ledYellow":
            led = elements.LedArduino()
            led.set_color(2)
            self.robot_elements.append(led)
        elif component == "ledGreen":
            led = elements.LedArduino()
            led.set_color(3)
            self.robot_elements.append(led)
        elif component == "buzzer":
            buzzer = elements.BuzzerArduino()
            self.robot_elements.append(buzzer)
        elif component == "ledRGB":
            led_rgb = elements.RGBArduino()
            self.robot_elements.append(led_rgb)
        elif component == "lightSensor":
            light_sensor = elements.LightSensorArduino()
            self.robot_elements.append(light_sensor)
        elif component == "PIRSensor":
            pir_sensor = elements.PIRSensorArduino()
            self.robot_elements.append(pir_sensor)
        elif component == "vibrationSensor":
            vibration_sensor = elements.VibrationSensorArduino()
            self.robot_elements.append(vibration_sensor)
        elif component == "infraredSensor":
            infrared_sensor = elements.InfraredSensorArduino()
            self.robot_elements.append(infrared_sensor)
        elif component == "ultrasonicSensor":
            ultrasonic_sensor = elements.UltrasoundSensorArduino()
            self.robot_elements.append(ultrasonic_sensor)
        elif component == "keyboard":
            keyboard = elements.KeyBoardArduino()
            self.robot_elements.append(keyboard)
        elif component == "screen":
            screen = elements.ScreenArduino()
            self.robot_elements.append(screen)
        elif component == "servomotor180":
            servomotor = elements.ServomotorArduino()
            self.robot_elements.append(servomotor)
        print(self.robot_elements)

    def assign_pins(self, pins):
        """
        Assigns the pins to the corresponding element
        Arguments:
            pins: a list of tuples with the name of the element,
            the corresponding pin and the element
        """
        for pin in pins:
            name = pin[0]
            pin = self.parse_pin(pin[1])
            element = pin[2]
            if name == "resistance1":
                self.set_resistance1(pin, element)
            elif name == "resistance2":
                self.set_resistance2(pin, element)
            elif name == "button1":
                self.set_button1(pin, element)
            elif name == "button2":
                self.set_button2(pin, element)
            elif name == "button3":
                self.set_button3(pin, element)
            elif name == "button4":
                self.set_button4(pin, element)
            elif name == "potentiometer1":
                self.set_potentiometer1(pin, element)
            elif name == "potentiometer2":
                self.set_potentiometer2(pin, element)
            elif name == "potentiometer3":
                self.set_potentiometer3(pin, element)
            elif name == "led1":
                self.set_led1(pin, element)
            elif name == "led2":
                self.set_led2(pin, element)
            elif name == "buzzer1":
                self.set_buzzer1(pin, element)
            elif name == "buzzer2":
                self.set_buzzer2(pin, element)
            elif name == "buzzer3":
                self.set_buzzer3(pin, element)
            elif name == "rgb1":
                self.set_rgb1(pin, element)
            elif name == "rgb2":
                self.set_rgb2(pin, element)
            elif name == "rgb3":
                self.set_rgb3(pin, element)
            elif name == "rgb4":
                self.set_rgb4(pin, element)
            elif name == "lightSensor1":
                self.set_light_sensor1(pin, element)
            elif name == "lightSensor2":
                self.set_light_sensor2(pin, element)
            elif name == "lightSensor3":
                self.set_light_sensor3(pin, element)
            elif name == "PIRSensor1":
                self.set_pir_sensor1(pin, element)
            elif name == "PIRSensor2":
                self.set_pir_sensor2(pin, element)
            elif name == "PIRSensor3":
                self.set_pir_sensor3(pin, element)
            elif name == "vibrationSensor1":
                self.set_vibration_sensor1(pin, element)
            elif name == "vibrationSensor2":
                self.set_vibration_sensor2(pin, element)
            elif name == "vibrationSensor3":
                self.set_vibration_sensor3(pin, element)
            elif name == "infraredSensor1":
                self.set_infrared_sensor1(pin, element)
            elif name == "infraredSensor2":
                self.set_infrared_sensor2(pin, element)
            elif name == "infraredSensor3":
                self.set_infrared_sensor3(pin, element)
            elif name == "ultrasonicSensor1":
                self.set_ultrasonic_sensor1(pin, element)
            elif name == "ultrasonicSensor2":
                self.set_ultrasonic_sensor2(pin, element)
            elif name == "ultrasonicSensor3":
                self.set_ultrasonic_sensor3(pin, element)
            elif name == "ultrasonicSensor4":
                self.set_ultrasonic_sensor4(pin, element)
            elif name == "keyboard1":
                self.set_keyboard1(pin, element)
            elif name == "keyboard2":
                self.set_keyboard2(pin, element)
            elif name == "keyboard3":
                self.set_keyboard3(pin, element)
            elif name == "keyboard4":
                self.set_keyboard4(pin, element)
            elif name == "keyboard5":
                self.set_keyboard5(pin, element)
            elif name == "keyboard6":
                self.set_keyboard6(pin, element)
            elif name == "keyboard7":
                self.set_keyboard7(pin, element)
            elif name == "keyboard8":
                self.set_keyboard8(pin, element)
            elif name == "screen1":
                self.set_screen2(pin, element)
            elif name == "screen2":
                self.set_screen3(pin, element)
            elif name == "screen3":
                self.set_screen1(pin, element)
            elif name == "screen4":
                self.set_screen4(pin, element)
            elif name == "servomotor1":
                self.set_servomotor1(pin, element)
            elif name == "servomotor2":
                self.set_servomotor2(pin, element)
            elif name == "servomotor3":
                self.set_servomotor3(pin, element)

    def set_resistance1(self, pin, resistance):
        """
        Attaches the pin 1 of a resistance to board pin
        Arguments:
            pin: the pin of the board
            resistance: the resistance to attach
        """
        if self.board.check_type(pin, resistance.get_pin1_type()):
            if self.board.attach_pin(pin, resistance):
                resistance.pin1 = pin

    def set_resistance2(self, pin, resistance):
        """
        Attaches the pin 2 of a resistance to board pin
        Arguments:
            pin: the pin of the board
            resistance: the resistance to attach
        """
        if self.board.check_type(pin, resistance.get_pin2_type()):
            if self.board.attach_pin(pin, resistance):
                resistance.pin2 = pin

    def set_button1(self, pin, button):
        """
        Attaches the pin 1 of a button to board pin
        Arguments:
            pin: the pin of the board
            button: the button to attach
        """
        if self.board.check_type(pin, button.get_pin1_type()):
            if self.board.attach_pin(pin, button):
                button.pin1 = pin

    def set_button2(self, pin, button):
        """
        Attaches the pin 2 of a button to board pin
        Arguments:
            pin: the pin of the board
            button: the button to attach
        """
        if self.board.check_type(pin, button.get_pin2_type()):
            if self.board.attach_pin(pin, button):
                button.pin2 = pin

    def set_button3(self, pin, button):
        """
        Attaches the pin 3 of a button to board pin
        Arguments:
            pin: the pin of the board
            button: the button to attach
        """
        if self.board.check_type(pin, button.get_pin3_type()):
            if self.board.attach_pin(pin, button):
                button.pin3 = pin

    def set_button4(self, pin, button):
        """
        Attaches the pin 4 of a button to board pin
        Arguments:
            pin: the pin of the board
            button: the button to attach
        """
        if self.board.check_type(pin, button.get_pin4_type()):
            if self.board.attach_pin(pin, button):
                button.pin4 = pin

    def set_potentiometer1(self, pin, potentiometer):
        """
        Attaches the pin 1 of a potentiometer to board pin
        Arguments:
            pin: the pin of the board
            potentiometer: the potentiometer to attach
        """
        if self.board.check_type(pin, potentiometer.get_pin1_type()):
            if self.board.attach_pin(pin, potentiometer):
                potentiometer.pin1 = pin

    def set_potentiometer2(self, pin, potentiometer):
        """
        Attaches the pin 2 of a potentiometer to board pin
        Arguments:
            pin: the pin of the board
            potentiometer: the potentiometer to attach
        """
        if self.board.check_type(pin, potentiometer.get_pin2_type()):
            if self.board.attach_pin(pin, potentiometer):
                potentiometer.pin2 = pin

    def set_potentiometer3(self, pin, potentiometer):
        """
        Attaches the pin 3 of a potentiometer to board pin
        Arguments:
            pin: the pin of the board
            potentiometer: the potentiometer to attach
        """
        if self.board.check_type(pin, potentiometer.get_pin3_type()):
            if self.board.attach_pin(pin, potentiometer):
                potentiometer.pin3 = pin

    def set_led1(self, pin, led):
        """
        Attaches the pin 1 of a LED to board pin
        Arguments:
            pin: the pin of the board
            led: the LED to attach
        """
        if self.board.check_type(pin, led.get_pin1_type()):
            if self.board.attach_pin(pin, led):
                led.pin1 = pin

    def set_led2(self, pin, led):
        """
        Attaches the pin 2 of a LED to board pin
        Arguments:
            pin: the pin of the board
            led: the LED to attach
        """
        if self.board.check_type(pin, led.get_pin2_type()):
            if self.board.attach_pin(pin, led):
                led.pin2 = pin

    def set_buzzer1(self, pin, buzzer):
        """
        Attaches the pin 1 of a buzzer to board pin
        Arguments:
            pin: the pin of the board
            buzzer: the buzzer to attach
        """
        if self.board.check_type(pin, buzzer.get_pin1_type()):
            if self.board.attach_pin(pin, buzzer):
                buzzer.pin1 = pin

    def set_buzzer2(self, pin, buzzer):
        """
        Attaches the pin 2 of a buzzer to board pin
        Arguments:
            pin: the pin of the board
            buzzer: the buzzer to attach
        """
        if self.board.check_type(pin, buzzer.get_pin2_type()):
            if self.board.attach_pin(pin, buzzer):
                buzzer.pin2 = pin

    def set_buzzer3(self, pin, buzzer):
        """
        Attaches the pin 3 of a buzzer to board pin
        Arguments:
            pin: the pin of the board
            buzzer: the buzzer to attach
        """
        if self.board.check_type(pin, buzzer.get_pin3_type()):
            if self.board.attach_pin(pin, buzzer):
                buzzer.pin3 = pin

    def set_rgb1(self, pin, rgb):
        """
        Attaches the pin 1 of a LED rgb to board pin
        Arguments:
            pin: the pin of the board
            rgb: the LED rgb to attach
        """
        if self.board.check_type(pin, rgb.get_pin1_type()):
            if self.board.attach_pin(pin, rgb):
                rgb.pin1 = pin

    def set_rgb2(self, pin, rgb):
        """
        Attaches the pin 2 of a LED rgb to board pin
        Arguments:
            pin: the pin of the board
            rgb: the LED rgb to attach
        """
        if self.board.check_type(pin, rgb.get_pin2_type()):
            if self.board.attach_pin(pin, rgb):
                rgb.pin2 = pin

    def set_rgb3(self, pin, rgb):
        """
        Attaches the pin 3 of a LED rgb to board pin
        Arguments:
            pin: the pin of the board
            rgb: the LED rgb to attach
        """
        if self.board.check_type(pin, rgb.get_pin3_type()):
            if self.board.attach_pin(pin, rgb):
                rgb.pin3 = pin

    def set_rgb4(self, pin, rgb):
        """
        Attaches the pin 4 of a LED rgb to board pin
        Arguments:
            pin: the pin of the board
            rgb: the LED rgb to attach
        """
        if self.board.check_type(pin, rgb.get_pin4_type()):
            if self.board.attach_pin(pin, rgb):
                rgb.pin4 = pin

    def set_light_sensor1(self, pin, light_sensor):
        """
        Attaches the pin 1 of a light sensor to board pin
        Arguments:
            pin: the pin of the board
            light_sensor: the light_sensor to attach
        """
        if self.board.check_type(pin, light_sensor.get_pin1_type()):
            if self.board.attach_pin(pin, light_sensor):
                light_sensor.pin1 = pin

    def set_light_sensor2(self, pin, light_sensor):
        """
        Attaches the pin 2 of a light sensor to board pin
        Arguments:
            pin: the pin of the board
            light_sensor: the light_sensor to attach
        """
        if self.board.check_type(pin, light_sensor.get_pin2_type()):
            if self.board.attach_pin(pin, light_sensor):
                light_sensor.pin2 = pin

    def set_light_sensor3(self, pin, light_sensor):
        """
        Attaches the pin 3 of a light sensor to board pin
        Arguments:
            pin: the pin of the board
            light_sensor: the light sensor to attach
        """
        if self.board.check_type(pin, light_sensor.get_pin3_type()):
            if self.board.attach_pin(pin, light_sensor):
                light_sensor.pin3 = pin

    def set_pir_sensor1(self, pin, pir_sensor):
        """
        Attaches the pin 1 of a PIR sensor to board pin
        Arguments:
            pin: the pin of the board
            pir_sensor: the PIR sensor to attach
        """
        if self.board.check_type(pin, pir_sensor.get_pin1_type()):
            if self.board.attach_pin(pin, pir_sensor):
                pir_sensor.pin1 = pin

    def set_pir_sensor2(self, pin, pir_sensor):
        """
        Attaches the pin 2 of a PIR sensor to board pin
        Arguments:
            pin: the pin of the board
            pir_sensor: the PIR sensor to attach
        """
        if self.board.check_type(pin, pir_sensor.get_pin2_type()):
            if self.board.attach_pin(pin, pir_sensor):
                pir_sensor.pin2 = pin

    def set_pir_sensor3(self, pin, pir_sensor):
        """
        Attaches the pin 3 of a PIR sensor to board pin
        Arguments:
            pin: the pin of the board
            pir_sensor: the PIR sensor to attach
        """
        if self.board.check_type(pin, pir_sensor.get_pin3_type()):
            if self.board.attach_pin(pin, pir_sensor):
                pir_sensor.pin3 = pin

    def set_vibration_sensor1(self, pin, vibration_sensor):
        """
        Attaches the pin 1 of a vibration sensor to board pin
        Arguments:
            pin: the pin of the board
            vibration_sensor: the vibration sensor to attach
        """
        if self.board.check_type(pin, vibration_sensor.get_pin1_type()):
            if self.board.attach_pin(pin, vibration_sensor):
                vibration_sensor.pin1 = pin

    def set_vibration_sensor2(self, pin, vibration_sensor):
        """
        Attaches the pin 2 of a vibration sensor to board pin
        Arguments:
            pin: the pin of the board
            vibration_sensor: the vibration sensor to attach
        """
        if self.board.check_type(pin, vibration_sensor.get_pin2_type()):
            if self.board.attach_pin(pin, vibration_sensor):
                vibration_sensor.pin2 = pin

    def set_vibration_sensor3(self, pin, vibration_sensor):
        """
        Attaches the pin 3 of a vibration sensor to board pin
        Arguments:
            pin: the pin of the board
            vibration_sensor: the vibration sensor to attach
        """
        if self.board.check_type(pin, vibration_sensor.get_pin3_type()):
            if self.board.attach_pin(pin, vibration_sensor):
                vibration_sensor.pin3 = pin

    def set_infrared_sensor1(self, pin, infrared_sensor):
        """
        Attaches the pin 1 of an infrared sensor to board pin
        Arguments:
            pin: the pin of the board
            infrared_sensor: the infrared sensor to attach
        """
        if self.board.check_type(pin, infrared_sensor.get_pin1_type()):
            if self.board.attach_pin(pin, infrared_sensor):
                infrared_sensor.pin1 = pin

    def set_infrared_sensor2(self, pin, infrared_sensor):
        """
        Attaches the pin 2 of an infrared sensor to board pin
        Arguments:
            pin: the pin of the board
            infrared_sensor: the infrared sensor to attach
        """
        if self.board.check_type(pin, infrared_sensor.get_pin2_type()):
            if self.board.attach_pin(pin, infrared_sensor):
                infrared_sensor.pin2 = pin

    def set_infrared_sensor3(self, pin, infrared_sensor):
        """
        Attaches the pin 3 of an infrared sensor to board pin
        Arguments:
            pin: the pin of the board
            infrared_sensor: the infrared sensor to attach
        """
        if self.board.check_type(pin, infrared_sensor.get_pin3_type()):
            if self.board.attach_pin(pin, infrared_sensor):
                infrared_sensor.pin3 = pin

    def set_ultrasonic_sensor1(self, pin, ultrasonic_sensor):
        """
        Attaches the pin 1 of an ultrasonic sensor to board pin
        Arguments:
            pin: the pin of the board
            ultrasonic_sensor: the ultrasonic sensor to attach
        """
        if self.board.check_type(pin, ultrasonic_sensor.get_pin1_type()):
            if self.board.attach_pin(pin, ultrasonic_sensor):
                ultrasonic_sensor.pin1 = pin

    def set_ultrasonic_sensor2(self, pin, ultrasonic_sensor):
        """
        Attaches the pin 2 of an ultrasonic sensor to board pin
        Arguments:
            pin: the pin of the board
            ultrasonic_sensor: the ultrasonic sensor to attach
        """
        if self.board.check_type(pin, ultrasonic_sensor.get_pin2_type()):
            if self.board.attach_pin(pin, ultrasonic_sensor):
                ultrasonic_sensor.pin2 = pin

    def set_ultrasonic_sensor3(self, pin, ultrasonic_sensor):
        """
        Attaches the pin 3 of an ultrasonic sensor to board pin
        Arguments:
            pin: the pin of the board
            ultrasonic_sensor: the ultrasonic sensor to attach
        """
        if self.board.check_type(pin, ultrasonic_sensor.get_pin3_type()):
            if self.board.attach_pin(pin, ultrasonic_sensor):
                ultrasonic_sensor.pin3 = pin

    def set_ultrasonic_sensor4(self, pin, ultrasonic_sensor):
        """
        Attaches the pin 4 of an ultrasonic sensor to board pin
        Arguments:
            pin: the pin of the board
            ultrasonic_sensor: the ultrasonic sensor to attach
        """
        if self.board.check_type(pin, ultrasonic_sensor.get_pin4_type()):
            if self.board.attach_pin(pin, ultrasonic_sensor):
                ultrasonic_sensor.pin4 = pin

    def set_keyboard1(self, pin, keyboard):
        """
        Attaches the pin 1 of a keyboard to board pin
        Arguments:
            pin: the pin of the board
            keyboard: the keyboard to attach
        """
        if self.board.check_type(pin, keyboard.get_pin1_type()):
            if self.board.attach_pin(pin, keyboard):
                keyboard.pin1 = pin

    def set_keyboard2(self, pin, keyboard):
        """
        Attaches the pin 2 of a keyboard to board pin
        Arguments:
            pin: the pin of the board
            keyboard: the keyboard to attach
        """
        if self.board.check_type(pin, keyboard.get_pin2_type()):
            if self.board.attach_pin(pin, keyboard):
                keyboard.pin2 = pin

    def set_keyboard3(self, pin, keyboard):
        """
        Attaches the pin 3 of a keyboard to board pin
        Arguments:
            pin: the pin of the board
            keyboard: the keyboard to attach
        """
        if self.board.check_type(pin, keyboard.get_pin3_type()):
            if self.board.attach_pin(pin, keyboard):
                keyboard.pin3 = pin

    def set_keyboard4(self, pin, keyboard):
        """
        Attaches the pin 4 of a keyboard to board pin
        Arguments:
            pin: the pin of the board
            keyboard: the keyboard to attach
        """
        if self.board.check_type(pin, keyboard.get_pin4_type()):
            if self.board.attach_pin(pin, keyboard):
                keyboard.pin4 = pin

    def set_keyboard5(self, pin, keyboard):
        """
        Attaches the pin 5 of a keyboard to board pin
        Arguments:
            pin: the pin of the board
            keyboard: the keyboard to attach
        """
        if self.board.check_type(pin, keyboard.get_pin5_type()):
            if self.board.attach_pin(pin, keyboard):
                keyboard.pin5 = pin

    def set_keyboard6(self, pin, keyboard):
        """
        Attaches the pin 6 of a keyboard to board pin
        Arguments:
            pin: the pin of the board
            keyboard: the keyboard to attach
        """
        if self.board.check_type(pin, keyboard.get_pin6_type()):
            if self.board.attach_pin(pin, keyboard):
                keyboard.pin6 = pin

    def set_keyboard7(self, pin, keyboard):
        """
        Attaches the pin 7 of a keyboard to board pin
        Arguments:
            pin: the pin of the board
            keyboard: the keyboard to attach
        """
        if self.board.check_type(pin, keyboard.get_pin7_type()):
            if self.board.attach_pin(pin, keyboard):
                keyboard.pin7 = pin

    def set_keyboard8(self, pin, keyboard):
        """
        Attaches the pin 8 of a keyboard to board pin
        Arguments:
            pin: the pin of the board
            keyboard: the keyboard to attach
        """
        if self.board.check_type(pin, keyboard.get_pin8_type()):
            if self.board.attach_pin(pin, keyboard):
                keyboard.pin8 = pin

    def set_screen1(self, pin, screen):
        """
        Attaches the pin 1 of a screen to board pin
        Arguments:
            pin: the pin of the board
            screen: the screen to attach
        """
        if self.board.check_type(pin, screen.get_pin1_type()):
            if self.board.attach_pin(pin, screen):
                screen.pin1 = pin

    def set_screen2(self, pin, screen):
        """
        Attaches the pin 2 of a screen to board pin
        Arguments:
            pin: the pin of the board
            screen: the screen to attach
        """
        if self.board.check_type(pin, screen.get_pin2_type()):
            if self.board.attach_pin(pin, screen):
                screen.pin2 = pin

    def set_screen3(self, pin, screen):
        """
        Attaches the pin 3 of a screen to board pin
        Arguments:
            pin: the pin of the board
            screen: the screen to attach
        """
        if self.board.check_type(pin, screen.get_pin3_type()):
            if self.board.attach_pin(pin, screen):
                screen.pin3 = pin

    def set_screen4(self, pin, screen):
        """
        Attaches the pin 4 of a screen to board pin
        Arguments:
            pin: the pin of the board
            screen: the screen to attach
        """
        if self.board.check_type(pin, screen.get_pin4_type()):
            if self.board.attach_pin(pin, screen):
                screen.pin4 = pin

    def set_servomotor1(self, pin, servomotor):
        """
        Attaches the pin 1 of a servomotor to board pin
        Arguments:
            pin: the pin of the board
            servomotor: the servomotor to attach
        """
        if self.board.check_type(pin, servomotor.get_pin1_type()):
            if self.board.attach_pin(pin, servomotor):
                servomotor.pin1 = pin

    def set_servomotor2(self, pin, servomotor):
        """
        Attaches the pin 2 of a servomotor to board pin
        Arguments:
            pin: the pin of the board
            servomotor: the servomotor to attach
        """
        if self.board.check_type(pin, servomotor.get_pin2_type()):
            if self.board.attach_pin(pin, servomotor):
                servomotor.pin2 = pin

    def set_servomotor3(self, pin, servomotor):
        """
        Attaches the pin 3 of a servomotor to board pin
        Arguments:
            pin: the pin of the board
            servomotor: the servomotor to attach
        """
        if self.board.check_type(pin, servomotor.get_pin3_type()):
            if self.board.attach_pin(pin, servomotor):
                servomotor.pin3 = pin
