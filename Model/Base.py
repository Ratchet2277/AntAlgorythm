import math
import numbers


class Entity:
    posX = 0
    posY = 0

    def __init__(self, pos_x: numbers, pos_y: numbers):
        self.posX = pos_x
        self.posY = pos_y

    def distance_from(self, pos_x: numbers, pos_y: numbers):
        x_diff = pos_x - self.posX
        y_diff = pos_y - self.posY
        return math.sqrt((x_diff ** 2) + (y_diff ** 2))
