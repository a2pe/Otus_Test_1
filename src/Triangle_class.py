from src.Figure_class import Figure
from math import sqrt


class Triangle(Figure):

    def __init__(self, side_2, side_3, side):
        super().__init__(side)
        self.side_1 = side
        self.side_2 = side_2
        self.side_3 = side_3
        self.name = 'Triangle'

    def general_check(self):
        if self.side_1 == 0 or self.side_2 == 0 or self.side_3 == 0:
            return "Triangle side cannot be zero"

    @property
    def area(self):
        self.general_check()
        p = (self.side_1 + self.side_2 + self.side_3) / 2
        if self.side_1 + self.side_2 <= self.side_3 or self.side_1 + self.side_3 <= self.side_2 or \
                self.side_2 + self.side_3 <= self.side_1:
            return "No Triangle with these parameters can be created"
        else:
            area = sqrt((p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)))
            return area

    @property
    def perimeter(self):
        self.general_check()
        return self.side_1 + self.side_2 + self.side_3
