import random

from src.Circle_class import Circle
from src.Figure_class import Figure
from src.Rectangle_class import Rectangle
from src.Square_class import Square
from src.Triangle_class import Triangle

import pytest


@pytest.fixture
def general_figure():
    figure = Figure(random.randint(1, 10))
    return figure


@pytest.fixture
def square_figure():
    square = Square(random.randint(1, 10))
    return square


@pytest.fixture
def rectangle_figure():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    rectangle = Rectangle(a, b)
    return rectangle


@pytest.fixture
def circle_figure():
    circle = Circle(random.randint(1, 100))
    return circle


@pytest.fixture
def triangle_figure():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    triangle = Triangle(a, b, c)
    return triangle
