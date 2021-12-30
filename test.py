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




    def test_servo_with_joystick(self):
      joystick = Joystick()
      key_q = False
      servo_pin = 32
      servo = PWM(pin=servo_pin)
      servo.start(0, 0.05)
      while not key_q:
          key_q = joystick.getJS('R2')
          left = joystick.getJS('axis3') * 45
          right = joystick.getJS('axis4') * 45
          if left:
            servo.angle(left)
          elif right:
            servo.angle(right)













if __name__ == '__main__':
    test_rc = TestModules()
    # test_rc.test_servo()
    # test_rc.test_brushless_motor()
    # test_rc.test_manual_values_esc()
    # test_rc.test_auto_calibrate()
    # test_rc.test_keyboard_input()
    test_rc.test_joysick_input()
