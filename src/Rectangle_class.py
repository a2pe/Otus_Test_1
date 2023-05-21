from src.Figure_class import Figure


class Rectangle(Figure):

    def __init__(self, side, side_2):
        super().__init__(side)
        self.name = 'Rectangle'
        self.side_2 = side_2

    def general_check(self):
        if self.side == 0 or self.side_2 == 0:
            return "No Rectangle with zero side can be created"

    @property
    def area(self):
        self.general_check()
        return self.side * self.side_2

    @property
    def perimeter(self):
        self.general_check()
        return (self.side * 2) * (self.side_2 * 2)
