from src.Figure_class import Figure
import math


class Circle(Figure):

    def __init__(self, side):
        super().__init__(side)
        self.name = 'Circle'

    @property
    def area(self):
        self.general_check()
        return self.side ** 2 * math.pi

    @property
    def perimeter(self):
        self.general_check()
        return 2 * math.pi * self.side
