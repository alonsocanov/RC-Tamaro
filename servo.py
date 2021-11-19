import Jetson.GPIO as GPIO
import time


class Servo:
    def __init__(self, pin=32, hz=100, min_duty_cycle=5, max_duty_cycle=25):
        # servo that I used the  duty cycle ranges is [5, 25]
        self.pin = pin
        self.hz = hz
        self.pwm = None
        self.min_duty_cycle = min_duty_cycle
        self.max_duty_cycle = max_duty_cycle


    def start(self):
        GPIO.setwarnings(False)
        # Set Jetson to use pin number when referencing GPIO pins.
        # Can use GPIO.setmode(GPIO.BCM) instead to use Broadcom SOC channel names.
        GPIO.setmode(GPIO.BOARD)
        # Set GPIO pin 12 to output mode.
        GPIO.setup(self.pin, GPIO.OUT)
        # Initialize PWM on pwmPin 100Hz frequency
        self.pwm = GPIO.PWM(self.pin, self.hz)
        self.pwm.start(0)
        time.sleep(0.05)

    def dutyCycleToAngle(self, angle: float) -> float:
        difference = self.max_duty_cycle - self.min_duty_cycle
        # wheel max angle
        wheel_liberty_angle = 90.
        # slope
        m = difference / wheel_liberty_angle
        # upper and lowe bound
        if angle > 45:
            angle = 45
        elif angle < -45:
            angle = -45
        # center offset
        offset = difference / 2.
        # duty cycle
        duty_cycle = (angle * m) + self.min_duty_cycle + offset
        return duty_cycle



    def angle(self, angle):
        # missing duty cycle conversion
        duty_cycle = self.dutyCycleToAngle(angle)
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.05)


    def cleanPWM(self):
        # stop PWM
        self.pwm.stop()
        # resets GPIO ports used back to input mode
        GPIO.cleanup()