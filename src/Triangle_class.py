from Otus_Test_1.src.Figure_class import Figure
from math import sqrt


class Triangle(Figure):

    def __init__(self, side_2, side_3, side):
        super().__init__(side)
        self.side_1 = side
        self.side_2 = side_2
        self.side_3 = side_3
        self.name = 'Triangle'
        self.general_check()

    def general_check(self):
        if self.side <= 0 or self.side_2 <= 0 or self.side_3 <= 0:
            raise ValueError("No Triangle can be created with zero or negative side value.")
        elif self.side_1 + self.side_2 <= self.side_3 or self.side_1 + self.side_3 <= self.side_2 or \
                self.side_2 + self.side_3 <= self.side_1:
            raise ValueError("No Triangle can be created with the specified sides.")

    @property
    def area(self):
        p = (self.side_1 + self.side_2 + self.side_3) / 2
        area = sqrt((p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3)))
        return float(f'{area:.2f}')

    @property
    def perimeter(self):
        perim = self.side_1 + self.side_2 + self.side_3
        return float(f'{perim:.2f}')
