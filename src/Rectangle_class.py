from Otus_Test_1.src.Figure_class import Figure


class Rectangle(Figure):

    def __init__(self, side, side_2):
        super().__init__(side)
        self.name = 'Rectangle'
        self.side_2 = side_2
        self.general_check()

    def general_check(self):
        if self.side <= 0 or self.side_2 <= 0:
            raise ValueError("No Rectangle with zero or negative side can be created")

    @property
    def area(self):
        return float(f'{self.side * self.side_2:.2f}')

    @property
    def perimeter(self):
        return float(f'{(self.side + self.side_2) * 2:.2f}')
