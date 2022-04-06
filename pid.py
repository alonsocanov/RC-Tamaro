import time


class PID:
    def __init__(self, k_p, k_i, k_d, direction=1) -> None:
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d
        self.direction = direction
        self.update_time = 100
        self.last_update = self.millis(self)
        self.output = 0.0
        self.p_output = 0.0
        self.i_output = 0.0
        self.d_output = 0.0
        self.last_actual = 0.0
        self.lower_integral_limit = 0
        self.upper_integral_limit = 0
        self.lower_ouput_limit = 0
        self.upper_output_limit = 0
        self.output_offset = 0

    def set_integral_limits(self, lower_limit, upper_limit):
        self.lower_integral_limit = lower_limit
        self.upper_integral_limit = upper_limit

    def setOutputLimits(self, lower_limit, upper_limit):
        self.lower_ouput_limit = lower_limit
        self.upper_output_limit = upper_limit

    def addOutputOffset(self, offset):
        self.outputOffset = offset

    @staticmethod
    def millis(self):
        return int(round(time.time() * 10000))

    def changeParameters(self, k_p, k_i, k_d):
        if self.direction < 0:
            self.k_p = k_p * -1
            self.k_i = k_i * -1
            self.k_d = k_d * -1
        else:
            self.k_p = k_p
            self.k_i = k_i
            self.k_d = k_d

    # def addOffset(self, offset):
    #     self.offset = offset

    def compute(self, target, actual):

        now = self.millis(self)
        time_difference = now - self.last_update
        if time_difference >= self.update_time:
            error = target - actual
            self.p_output = error * self.k_p
            self.i_output += error * self.k_i
            self.d_output += actual - self.last_actual

            if self.i_output < self.lower_integral_limit:
                self.i_output = self.lower_integral_limit
            elif self.i_output > self.upper_integral_limit:
                self.i_output = self.upper_integral_limit

            self.output = self.output_offset + self.p_output + self.i_output + self.d_output

            if self.output < self.lower_ouput_limit:
                self.output = self.lower_ouput_limit
            elif self.output > self.upper_output_limit:
                self.output = self.upper_output_limit

            self.last_actual = actual
            self.last_update = now

        return self.output
