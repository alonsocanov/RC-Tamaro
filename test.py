import unittest
from pwm_control import PWM
import time


class TestModules(unittest.TestCase):

    def test_servo(self):
        print('Testing Servo for stearing')
        servo_pin = 32
        servo = PWM(pin=servo_pin)
        servo.start()
        servo.angle(-45)
        servo.cleanPWM()

    def test_brushless_motor(self):
      print('Testing Brushless Motor')
      motor_pin = 33
      motor = PWM(pin=motor_pin, hz=50, min_duty_cycle=0, max_duty_cycle=100)
      motor.start()
      time.sleep(10)
      motor.setDutyCycle(3)
      time.sleep(10)
      for percentage in range(3, 1000, 1):
        print(percentage * .1)
        motor.setDutyCycle(percentage * .1)











if __name__ == '__main__':
    test_rc = TestModules()
    # test_rc.test_servo()
    test_rc.test_brushless_motor()
