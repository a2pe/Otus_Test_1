class Figure:

    def __init__(self, side):
        self.side = side
        self.name = 'Figure'

    def general_check(self):
        if self.side == 0:
            return "Figure side cannot be zero"

    @property
    def area(self):
        self.general_check()
        return self.side * self.side

    def add_area(self, figure_2):
        if not isinstance(figure_2, Figure):
            raise ValueError("Not a geometrical figure!")
        else:
            total_figure_sum = self.area + figure_2.area
            return total_figure_sum

