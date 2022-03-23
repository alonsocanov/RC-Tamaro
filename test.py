import unittest
from pwm_control import PWM
import Jetson.GPIO as GPIO
from keyboard import Keyboard
from joystick import Joystick
from i2c import I2C
from system_data import get_ip_address
from pid import Pid
import time


class TestModules(unittest.TestCase):

    def test_servo(self):
        print('Testing Servo for stearing')
        servo_pin = 32
        servo = PWM(pin=servo_pin)
        servo.start(0, 0.05)
        servo.angle(45)
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

    def test_motors_with_joystick(self):
      motor_pin = 33
      hz = 100
      motor = PWM(motor_pin, hz=hz, min_duty_cycle=1, max_duty_cycle=10)
      motor.start(1)
      # motor.autoCalibrate()

      joystick = Joystick()
      key_q = False
      servo_pin = 32
      servo = PWM(pin=servo_pin)
      servo.start(0, 0.05)
      while not key_q:
          key_q = joystick.getJS(['R2'])[0]
          _, up, left, right  = joystick.getJS(['axis1', 'axis2', 'axis3', 'axis4'])
          print(up, left, right)
          if left:
            servo.angle(left * 45)
          elif right:
            servo.angle(right * 45)
          if up > 0:
            motor.percentage(40)
          elif up < 0:
            motor.percentage(0)

    def test_oled(self):
      text = get_ip_address('wlan0')
      oled = I2C()
      oled.set_display(0x3c)
      oled.draw_display(text, (1, 1))

    def test_pid(self):
      pid = Pid(k_p=2.0, k_i=0.0, k_d=0.0, direction=1)
      pid.addOutputOffset(0)
      pid.update_time = 100
      pid.setOutputLimits(-45, 45)

      while(True):
          output = pid.compute(0, 100)
          print(output)


if __name__ == '__main__':
    test_rc = TestModules()
    # test_rc.test_servo()
    # test_rc.test_brushless_motor()
    # test_rc.test_manual_values_esc()

    # test_rc.test_auto_calibrate()
    # test_rc.test_keyboard_input()
    # test_rc.test_joysick_input()
    test_rc.test_motors_with_joystick()
    # test_rc.test_oled()
    # test_rc.test_pid()
