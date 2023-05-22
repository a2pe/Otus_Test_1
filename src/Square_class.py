from Otus_Test_1.src.Figure_class import Figure


class Square(Figure):

    def __init__(self, side):
        super().__init__(side)
        self.name = 'Square'
        self.general_check()

    def general_check(self):
        if self.side <= 0:
            raise ValueError("No Square can be created with this side.")

    @property
    def area(self):
        self.general_check()
        return float(f'{self.side ** 2:.2f}')

    @property
    def perimeter(self):
        self.general_check()
        return float(f'{self.side * 4:.2f}')
