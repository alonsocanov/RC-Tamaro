import unittest
from pwm_control import PWM
import Jetson.GPIO as GPIO
from keyboard import Keyboard
from joystick import Joystick
import time


class TestModules(unittest.TestCase):

    def test_servo(self):
        print('Testing Servo for stearing')
        servo_pin = 32
        servo = PWM(pin=servo_pin)
        servo.start(0, 0.05)
        servo.angle(-45)
        servo.cleanPWM()

    def test_brushless_motor(self):
      print('Testing Brushless Motor')
      motor_pin = 33
      motor = PWM(motor_pin, min_duty_cycle=1, max_duty_cycle=10)
      motor.start(0, 2)
      for x in range(1, 100):
        print(x)
        motor.percentage(x)

      for x in reversed(range(1, 100)):
        print(x)
        motor.percentage(x)

    def test_manual_values_esc(self):
      print('Testing Brushless Motor')
      motor_pin = 33
      hz = 100
      motor = PWM(motor_pin, hz=hz, min_duty_cycle=1, max_duty_cycle=10)
      motor.start(1)
      motor.setManualValues()

    def test_auto_calibrate(self):
      motor_pin = 33
      hz = 100
      motor = PWM(motor_pin, hz=hz, min_duty_cycle=1, max_duty_cycle=10)
      motor.start(1)
      motor.autoCalibrate()

    def test_keyboard_input(self):
      keyboard = Keyboard()
      key_q = False
      t = time.time()
      while not key_q:
          key_q = keyboard.key_q()
          data = keyboard.arrow_control()
          if data:
            print(data)



    def test_joysick_input(self):
        joystick = Joystick()
        key_q = False
        t = time.time()
        while not key_q:
            key_q = joystick.getJS('R2')
            data_1 = joystick.getJS('axis2')
            data_2 = joystick.getJS('axis1')
            data = [data_1, data_2]
            if data_1 != 0 or data_2 != 0:
                print(data)













if __name__ == '__main__':
    test_rc = TestModules()
    # test_rc.test_servo()
    # test_rc.test_brushless_motor()
    # test_rc.test_manual_values_esc()
    # test_rc.test_auto_calibrate()
    # test_rc.test_keyboard_input()
    test_rc.test_joysick_input()
