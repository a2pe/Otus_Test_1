import pytest

from src.Circle_class import Circle
from src.Rectangle_class import Rectangle
from src.Square_class import Square
from src.Triangle_class import Triangle


def test_figure_general_creation(general_figure):
    """Testing Figure attributes"""
    assert general_figure.name == "Figure"


def test_square_creation(square_figure):
    """Testing Square attributes"""
    assert square_figure.name == "Square"


def test_square_area_and_perimeter():
    """Testing calculation of Square area and perimeter"""
    square = Square(3)
    assert square.area == 9
    assert square.perimeter == 12


def test_square_zero_value():
    """Testing  square creation with the side equal to 0"""
    square = Square(0)
    assert print(square.area) == print("Figure side cannot be zero")


def test_square_add_another_square_area():
    """Testing adding square area to another square area"""
    square = Square(4)
    assert square.add_area(square) == 32


def test_square_add_another_figure_area():
    """Testing adding square area to another square area"""
    square = Square(4)
    triangle = Triangle(4, 2, 5)
    assert square.add_area(triangle) == 19.799671038392667


def test_circle_creation(circle_figure):
    """Testing Circle attributes"""
    assert circle_figure.name == "Circle"


def test_circle_area_and_perimeter():
    """Testing calculation of Circle area and perimeter"""
    circle = Circle(4)
    assert circle.area == 50.26548245743669
    assert circle.perimeter == 25.132741228718345


def test_circle_add_another_figure():
    """Testing adding another figure area to the circle area """
    circle = Circle(10)
    rectangle = Rectangle(4, 20)
    assert circle.add_area(rectangle) == 394.1592653589793


def test_rectangle_creation(rectangle_figure):
    """Testing Rectangle attributes"""
    assert rectangle_figure.name == "Rectangle"


def test_rectangle_area_and_perimeter():
    """Testing calculation of Rectangle area and perimeter"""
    rectangle = Rectangle(11, 3)
    assert rectangle.area == 33
    assert rectangle.perimeter == 132


def test_rectangle_add_another_figure():
    """Testing adding another figure area to the rectangle area """
    rectangle = Rectangle(10, 4)
    triangle = Triangle(4, 2, 3)
    assert rectangle.add_area(triangle) == 42.90473750965556


def test_triangle_creation(triangle_figure):
    """Testing Triangle attributes"""
    assert triangle_figure.name == "Triangle"


def test_triangle_area_and_perimeter():
    """Testing Triangle area and perimeter calculations"""
    triangle = Triangle(4, 2, 3)
    assert triangle.area == 2.9047375096555625
    assert triangle.perimeter == 9


def test_triangle_add_another_figure_area():
    """Testing adding another figure area to the triangle area"""
    triangle = Triangle(4, 2, 3)
    square = Square(4)
    assert triangle.add_area(square) == 18.90473750965556


def test_value_error_triangle():
    """Testing area calculation for the triangle with incorrect sides"""
    triangle = Triangle(1, 2, 3)
    assert print(triangle.area) == print("No Triangle with these parameters can be created")


def test_triangle_zero_value():
    """Testing triangle and square creation with their sides equal to 0"""
    triangle = Triangle(0, 1, 2)
    assert print(triangle.area) == print("Triangle side cannot be zero")


def test_figure_value_error():
    """Testing adding area for non-geometrical figure"""
    square = Square(4)
    test_figure = "test_figure"
    with pytest.raises(ValueError, match="Not a geometrical figure!"):
        print(square.add_area(test_figure))
