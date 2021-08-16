import math
import numbers
import random
from abc import ABC, abstractmethod

import Model.Base
from Model.Enum.Types import AntType, TargetType, MarkType
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

    @abstractmethod
    def drop_mark(self) -> Mark:
        pass


class ExplorerAnt(BaseAnt):
    orientationVariation = 5

    def __init__(self, ant_type: AntType, pos_x: numbers, pos_y: numbers, orientation: numbers, target: TargetType):
        super().__init__(ant_type, pos_x, pos_y, orientation)
        if et not in [TargetType.Explore, TargetType.Home]:
            raise ValueError("target can only be Explore or Home for Explorer ants")
        self.target = target

    def chose_orientation(self, close_marks: Sequence[Mark]):
        if len(close_marks) == 0:
            return

        # if exploring, add randomness to movement
        if self.target == TargetType.Explore:
            self.orientation %= 360
            self.orientation += random.randrange(-self.orientationVariation, self.orientationVariation)

        mark_weight: Sequance[tulp[numbers, numbers]] = Array

        for i, mark in close_marks:
            delta_x = mark.posX - self.posX
            delta_y = mark.posY - self.posY
            angle = math.atan2(delta_y, delta_x)
            weight = 1 - abs((((angle - self.orientation) + 180) % 360 - 180) / 180)
            mark_weight.push((weight, angle))

        mark_weight.sort(key=lambda tup: tup[0])

        new_angle = sum([(x[0] * x[1]) for x in mark_weight])
        dividend = sum([x[0] for x in mark_weight])

        new_angle += self.orientation
        dividend += 1

        if dividend != 0:
            new_angle /= dividend

        self.orientation = new_angle

    def drop_mark(self) -> Mark:
        type = MarkType.Explored if self.target == TargetType.Explore else MarkType.FoodFound
        return Mark(type, self.pos_x, self.pos_y)
