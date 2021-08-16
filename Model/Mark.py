import numbers

from Model.Base import Entity
from Model.Enum.Types import MarkType


class Mark(Entity):
    strength = 100

    def __init__(self, type: MarkType, pos_x: numbers, pos_y: numbers):
        super().__init__(pos_x, pos_y)
        self.type = type

    def decay(self):
        self.strength -= 1
