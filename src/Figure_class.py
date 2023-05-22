
class Figure:

    def __init__(self, side):
        self.side = side
        self.name = 'Figure'

    def general_check(self):
        if self.side <= 0:
            return "Figure side cannot be of zero or negative value"

    # noinspection PyPropertyDefinition
    @property
    def area(self) -> float:
        pass

    def add_area(self, figure_2):
        if not isinstance(figure_2, Figure):
            raise ValueError("Not a geometrical figure!")
        else:
            total_figure_sum = float(self.area) + float(figure_2.area)
            return float(f'{total_figure_sum:.2f}')

