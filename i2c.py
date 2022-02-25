class I2C:
    def __init__(self, address):
        self.__address = address

    def get_address(self):
        return self.__address
