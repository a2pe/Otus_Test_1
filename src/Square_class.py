from src.Figure_class import Figure


class Square(Figure):

    def __init__(self, side):
        super().__init__(side)
        self.name = 'Square'

    @property
    def area(self):
        self.general_check()
        return self.side ** 2

    @property
    def perimeter(self):
        self.general_check()
        return self.side * 4
