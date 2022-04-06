from board import SCL, SDA
import busio
# Import the mpu6050 module
import adafruit_mpu6050


class IMU:
    def __init__(self):
        # Create the I2C interface.
        self.__i2c = busio.I2C(SCL, SDA)

    def set_imu(self):
        self.__mpu = adafruit_mpu6050.MPU6050(self.__i2c)

    def get_accleration(self):
        return self.__mpu.acceleration

    def get_gyro(self):
        return self.__mpu.gyro

    def get_temperature(self):
        return self.__mpu.temperature
