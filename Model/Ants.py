import math
import numbers
import random
from abc import ABC, abstractmethod

import Model.Base
from Model.Enum.Types import AntType, TargetType
from Model.Mark import Mark


class BaseAnt(Model.Base.Entity, ABC):
    orientation: numbers = 0
    type: AntType = ''
    lastMark: Mark = None
    target: TargetType = None

    def __init__(self, ant_type: AntType, pos_x: numbers, pos_y: numbers, orientation: numbers):
        super().__init__(pos_x, pos_y)
        self.type = ant_type
        self.orientation = abs(orientation) % 360

    @abstractmethod
    def chose_orientation(self, closest_mark: Mark):
        pass


class ExplorerAnt(BaseAnt):
    orientationVariation = 5

    def __init__(self, ant_type: AntType, pos_x: numbers, pos_y: numbers, orientation: numbers, target: TargetType):
        super().__init__(ant_type, pos_x, pos_y, orientation)
        if target not in [TargetType.Explore, TargetType.Home]:
            raise ValueError("target can only be Explore or Home for Explorer ants")
        self.target = target

    def chose_orientation(self, closest_mark: Mark):
        delta_x = Mark.posX - self.posX
        delta_y = Mark.posY - self.posY
        angle = math.atan2(delta_y, delta_x)
        self.orientation = angle

        # if exploring, add randomness to movement
        if self.target == TargetType.Explore:
            self.orientation += 180
            self.orientation %= 360
            self.orientation += random.randrange(-self.orientationVariation, self.orientationVariation)
