import pygame
import sys

class Joystick:
    def __init__(self):
        pygame.init()
        # control number
        try:
            self.controller = pygame.joystick.Joystick(0)
            self.controller.init()
        except pygame.error as error:
            print('Joystick not connected...')
            print(error)
            sys.exit(1)

        self.button = {'x': 0, 'o': 0, 't': 0, 's': 0, 'L1': 0, 'R1': 0, 'L2': 0,
                       'R2': 0, 'axis1': 0., 'axis2': 0., 'axis3': 0., 'axis4': 0.}
        self.axiss = [0., 0., 0., 0., 0., 0.]

    def getJS(self, name=''):
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                self.axiss[event.axis] = round(event.value, 2)
            elif event.type == pygame.JOYBUTTONDOWN:
                for x, (key, val) in enumerate(self.button.items()):
                    if x < 10:
                        if self.controller.get_button(x):
                            self.button[key] = 1
            elif event.type == pygame.JOYBUTTONUP:
                for x, (key, val) in enumerate(self.button.items()):
                    if x < 10:
                        if event.button == x:
                            self.button[key] = 0
        ''' up/down axis1/axis2 1/-1, left/right axis3/axis4 -1/1'''
        self.button['axis1'] = self.axiss[0] * -1
        self.button['axis2'] = self.axiss[1] * -1
        self.button['axis3'] = self.axiss[2] * -1
        self.button['axis4'] = self.axiss[3] * -1

        if not name:
            return self.button
        else:
            return self.button[name]