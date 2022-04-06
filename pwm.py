import Jetson.GPIO as GPIO
import time


class PWM:
    def __init__(self, pin=32, hz=100, min_duty_cycle=5, max_duty_cycle=25):
        # servo that I used the  duty cycle ranges is [5, 25]
        # for ESC the range of duty cycle is [1, 10]
        self.pin = pin
        self.hz = hz
        self.pwm = None
        self.min_duty_cycle = min_duty_cycle
        self.max_duty_cycle = max_duty_cycle
        GPIO.cleanup()

    def start(self, duty_cycle=0, sleep=0.05):

        GPIO.setwarnings(False)
        # Set Jetson to use pin number when referencing GPIO pins.
        # Can use GPIO.setmode(GPIO.BCM) instead to use Broadcom SOC channel names.
        GPIO.setmode(GPIO.BOARD)
        # Set GPIO pin 12 to output mode.
        GPIO.setup(self.pin, GPIO.OUT)
        # Initialize PWM on pwmPin 100Hz frequency
        self.pwm = GPIO.PWM(self.pin, self.hz)
        self.pwm.start(duty_cycle)
        time.sleep(sleep)

    def angleToDutyCycle(self, angle: float) -> float:
        difference = self.max_duty_cycle - self.min_duty_cycle
        # wheel max angle
        wheel_liberty_angle = 90.
        # slope
        m = difference / wheel_liberty_angle
        # upper and lower bound
        if angle > 45:
            angle = 45
        elif angle < -45:
            angle = -45
        # center offset
        offset = difference / 2.
        # duty cycle
        duty_cycle = (angle * m) + self.min_duty_cycle + offset
        return duty_cycle

    def percentageToDutyCycle(self, percentage: float) -> float:
        difference = self.max_duty_cycle - self.min_duty_cycle
        # wheel max angle
        liberty_percentage = 100.
        # slope
        m = difference / liberty_percentage
        # upper and lower bound
        if percentage > 100:
            percentage = 100
        elif percentage < 0:
            percentage = 0
        # duty cycle
        duty_cycle = (percentage * m) + self.min_duty_cycle
        return duty_cycle

    def setDutyCycle(self, value):
        self.pwm.ChangeDutyCycle(value)

    def angle(self, angle, sleep=0.05):
        # duty cycle conversion
        duty_cycle = self.angleToDutyCycle(angle)
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(sleep)

    def percentage(self, percentage, sleep=0.5):
        # duty cycle conversion
        duty_cycle = self.percentageToDutyCycle(percentage)
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(sleep)

    def cleanPWM(self):
        # stop PWM
        self.pwm.stop()
        # resets GPIO ports used back to input mode
        GPIO.cleanup()

    def setManualValues(self):
        """
        To calibrate before connecting the ESC and enter 99 then connect ESC, wait for beeps and then enter 1 and whait for beeps, then disconnect. Once disconnected reconnect and set any value between [1;100] and the ESC should be calibrated
        """
        while True:
            try:
                value = input("Enter number between 1-100\n")
            except KeyboardInterrupt:
                break
            try:
                i = int(value)
            except:
                break
            if i >= 1 and i <= 100:
                self.percentage(i)
            else:
                break

        print("End maual setup")

    def autoCalibrate(self):
        """
        To calibrate before connecting the ESC and enter 99 then connect ESC, wait for beeps and then enter 1 and whait for beeps, then disconnect. Once disconnected reconnect and set any value between [1;100] and the ESC should be calibrated
        """
        print("Connect ESC, you have 5 seconds")
        self.percentage(99, 5)

        self.percentage(1, 3)
        self.percentage(50, 10)

        print("End of calibration")
