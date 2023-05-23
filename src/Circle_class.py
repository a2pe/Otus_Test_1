from Otus_Test_1.src.Figure_class import Figure
import math


class Circle(Figure):

    def __init__(self, side):
        super().__init__(side)
        self.name = 'Circle'
        self.general_check()

    @property
    def area(self):
        return float(f'{self.side ** 2 * math.pi:.2f}')

    @property
    def perimeter(self):
        return float(f'{2 * math.pi * self.side:.2f}')
