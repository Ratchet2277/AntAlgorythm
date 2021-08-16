from enum import Enum


class AntType(Enum):
    Explorer = 0
    Worker = 1


class MarkType(Enum):
    Explored = 0
    FoodFound = 1


class TargetType(Enum):
    Explore = 0
    Home = 1
    Food = 2
