from servo import Servo


def main():
  servo_pin = 32
  servo = Servo(pin=servo_pin)
  servo.start()
  servo.angle(0)
  servo.cleanPWM()






if __name__ == '__main__':
  main()