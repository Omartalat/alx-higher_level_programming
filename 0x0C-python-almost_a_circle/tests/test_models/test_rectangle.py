#!/usr/bin/python3
"""
Defines unittests for models/rectangle.py.
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        """Test if Rectangle is an instance of Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """Test if Rectangle raises TypeError when called with no arguments."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test if Rectangle raises TypeError when called with one argument."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test if Rectangle assigns correct id when called with two arguments."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """Test if Rectangle assigns correct id when called with three arguments."""
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """Test if Rectangle assigns correct id when called with four arguments."""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """Test if Rectangle assigns correct id when called with five arguments."""
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """Test if Rectangle raises TypeError when called with more than five arguments."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """Test if Rectangle raises AttributeError when trying to access private attribute __width."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        """Test if Rectangle raises AttributeError when trying to access private attribute __height."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        """Test if Rectangle raises AttributeError when trying to access private attribute __x."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        """Test if Rectangle raises AttributeError when trying to access private attribute __y."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """Test the getter method for width attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        """Test the setter method for width attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        """Test the getter method for height attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        """Test the setter method for height attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        """Test the getter method for x attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        """Test the setter method for x attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        """Test the getter method for y attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        """Test the setter method for y attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangleWidth(unittest.TestCase):
    """Unittests for testing initialization of Rectangle width attribute."""

    def test_None_width(self):
        """Test if Rectangle raises TypeError when width is None."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        """Test if Rectangle raises TypeError when width is a string."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        """Test if Rectangle raises TypeError when width is a float."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    # Add more test cases for different invalid width values...


class TestRectangleHeight(unittest.TestCase):
    """Unittests for testing initialization of Rectangle height attribute."""

    def test_None_height(self):
        """Test if Rectangle raises TypeError when height is None."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        """Test if Rectangle raises TypeError when height is a string."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_float_height(self):
        """Test if Rectangle raises TypeError when height is a float."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    # Add more test cases for different invalid height values...


class TestRectangleX(unittest.TestCase):
    """Unittests for testing initialization of Rectangle x attribute."""

    def test_None_x(self):
        """Test if Rectangle raises TypeError when x is None."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        """Test if Rectangle raises TypeError when x is a string."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        """Test if Rectangle raises TypeError when x is a float."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    # Add more test cases for different invalid x values...


class TestRectangleY(unittest.TestCase):
    """Unittests for testing initialization of Rectangle y attribute."""

    def test_None_y(self):
        """Test if Rectangle raises TypeError when y is None."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        """Test if Rectangle raises TypeError when y is a string."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        """Test if Rectangle raises TypeError when y is a float."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    # Add more test cases for different invalid y values...


class TestRectangleOrderOfInitialization(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        """Test if Rectangle raises TypeError when width is initialized before height."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        """Test if Rectangle raises TypeError when width is initialized before x."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, "invalid x")

    def test_width_before_y(self):
        """Test if Rectangle raises TypeError when width is initialized before y."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")


class TestRectangleInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        """Test if Rectangle is an instance of Base."""
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        """Test if Rectangle raises TypeError when called with no arguments."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """Test if Rectangle raises TypeError when called with one argument."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        """Test if Rectangle assigns correct id when called with two arguments."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        """Test if Rectangle assigns correct id when called with three arguments."""
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        """Test if Rectangle assigns correct id when called with four arguments."""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        """Test if Rectangle assigns correct id when called with five arguments."""
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        """Test if Rectangle raises TypeError when called with more than five arguments."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        """Test if Rectangle raises AttributeError when trying to access private attribute __width."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        """Test if Rectangle raises AttributeError when trying to access private attribute __height."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        """Test if Rectangle raises AttributeError when trying to access private attribute __x."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        """Test if Rectangle raises AttributeError when trying to access private attribute __y."""
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        """Test the getter method for width attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        """Test the setter method for width attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        """Test the getter method for height attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        """Test the setter method for height attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        """Test the getter method for x attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        """Test the setter method for x attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        """Test the getter method for y attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        """Test the setter method for y attribute."""
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangleArea(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_area_small(self):
        """Test if area method returns the correct area for a small rectangle."""
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_large(self):
        """Test if area method returns the correct area for a large rectangle."""
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_changed_attributes(self):
        """Test if area method returns the correct area after changing rectangle attributes."""
        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_area_one_arg(self):
        """Test if area method raises TypeError when called with an argument."""
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangleStrAndDisplay(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.

        Returns:
            The text printed to stdout by calling method on rect.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_width_height(self):
        """Test if __str__ method prints the correct string representation with width and height."""
        r = Rectangle(4, 6)
        capture = TestRectangleStrAndDisplay.capture_stdout(r, "print")
        correct = "[Rectangle] ({}) 0/0 - 4/6\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        """Test if __str__ method prints the correct string representation with width, height, and x."""
        r = Rectangle(5, 5, 1)
        correct = "[Rectangle] ({}) 1/0 - 5/5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_width_height_x_y(self):
        """Test if __str__ method prints the correct string representation with width, height, x, and y."""
        r = Rectangle(1, 8, 2, 4)
        correct = "[Rectangle] ({}) 2/4 - 1/8".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_width_height_x_y_id(self):
        """Test if __str__ method prints the correct string representation with all attributes."""
        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

    def test_str_method_changed_attributes(self):
        """Test if __str__ method prints the correct string representation after changing attributes."""
        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

    def test_str_method_one_arg(self):
        """Test if __str__ method raises TypeError when called with an argument."""
        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    def test_display_width_height(self):
        """Test if display method prints the correct rectangle with width and height."""
        r = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangleStrAndDisplay.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        """Test if display method prints the correct rectangle with width, height, and x."""
        r = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangleStrAndDisplay.capture_stdout(r, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        """Test if display method prints the correct rectangle with width, height, and y."""
        r = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangleStrAndDisplay.capture_stdout(r, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        """Test if display method prints the correct rectangle with width, height, x, and y."""
        r = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangleStrAndDisplay.capture_stdout(r, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        """Test if display method raises TypeError when called with an argument."""
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


class TestRectangleUpdateArgs(unittest.TestCase):
    """Unittests for testing update args method of the Rectangle class."""

    def test_update_args_zero(self):
        """Test if update method assigns the correct attributes when called with zero arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))

    def test_update_args_one(self):
        """Test if update method assigns the correct attributes when called with one argument."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))

    def test_update_args_two(self):
        """Test if update method assigns the correct attributes when called with two arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))

    def test_update_args_three(self):
        """Test if update method assigns the correct attributes when called with three arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_args_four(self):
        """Test if update method assigns the correct attributes when called with four arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))

    def test_update_args_five(self):
        """Test if update method assigns the correct attributes when called with five arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_more_than_five(self):
        """Test if update method assigns the correct attributes when called with more than five arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_update_args_None_id(self):
        """Test if update method assigns correct id when called with None as the first argument."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        """Test if update method assigns correct attributes when called with None as the first argument and additional arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None, 4, 5, 2)
        correct = "[Rectangle] ({}) 2/10 - 4/5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        """Test if update method updates attributes correctly when called multiple times."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5, 6)
        r.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_args_invalid_width_type(self):
        """Test if update method raises TypeError when width is not an integer."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_width_zero(self):
        """Test if update method raises ValueError when width is zero."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    def test_update_args_width_negative(self):
        """Test if update method raises ValueError when width is negative."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, -5)

    def test_update_args_invalid_height_type(self):
        """Test if update method raises TypeError when height is not an integer."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 2, "invalid")

    def test_update_args_height_zero(self):
        """Test if update method raises ValueError when height is zero."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, 0)

    def test_update_args_height_negative(self):
        """Test if update method raises ValueError when height is negative."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(89, 1, -5)

    def test_update_args_invalid_x_type(self):
        """Test if update method raises TypeError when x is not an integer."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        """Test if update method raises ValueError when x is negative."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, 1, 2, -6)

    def test_update_args_invalid_y(self):
        """Test if update method raises TypeError when y is not an integer."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        """Test if update method raises ValueError when y is negative."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        """Test if update method raises TypeError when width is assigned before height."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        """Test if update method raises TypeError when width is assigned before x."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        """Test if update method raises TypeError when width is assigned before y."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        """Test if update method raises TypeError when height is assigned before x."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        """Test if update method raises TypeError when height is assigned before y."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(89, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        """Test if update method raises TypeError when x is assigned before y."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, 1, 2, "invalid", "invalid")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Rectangle class."""

    def test_update_kwargs_one(self):
        """Test if update method assigns the correct attributes when called with one keyword argument."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    def test_update_kwargs_two(self):
        """Test if update method assigns the correct attributes when called with two keyword arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 10/10 - 2/10", str(r))

    def test_update_kwargs_three(self):
        """Test if update method assigns the correct attributes when called with three keyword arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(width=2, height=3, id=89)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))

    def test_update_kwargs_four(self):
        """Test if update method assigns the correct attributes when called with four keyword arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def test_update_kwargs_five(self):
        """Test if update method assigns the correct attributes when called with five keyword arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, y=5, height=2, x=3, width=4)
        self.assertEqual("[Rectangle] (89) 3/5 - 4/2", str(r))

    def test_update_kwargs_more_than_five(self):
        """Test if update method assigns the correct attributes when called with more than five keyword arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, y=5, height=2, x=3, width=4, invalid=6)
        self.assertEqual("[Rectangle] (89) 3/5 - 4/2", str(r))

    def test_update_kwargs_None_id(self):
        """Test if update method assigns correct id when called with None as the id keyword argument."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = "[Rectangle] ({}) 10/10 - 10/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        """Test if update method assigns correct attributes when called with None as the id keyword argument and additional arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None, x=4, y=5, width=2)
        correct = "[Rectangle] ({}) 4/5 - 2/10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        """Test if update method updates attributes correctly when called multiple times."""
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=89, width=2, height=3, x=4, y=5)
        r.update(id=6, width=5, height=4, x=3, y=2)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(r))

    def test_update_kwargs_invalid_width_type(self):
        """Test if update method raises TypeError when width keyword argument is not an integer."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        """Test if update method raises ValueError when width keyword argument is zero."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=0)

    def test_update_kwargs_width_negative(self):
        """Test if update method raises ValueError when width keyword argument is negative."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        """Test if update method raises TypeError when height keyword argument is not an integer."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        """Test if update method raises ValueError when height keyword argument is zero."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=0)

    def test_update_kwargs_height_negative(self):
        """Test if update method raises ValueError when height keyword argument is negative."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(height=-5)

    def test_update_kwargs_invalid_x_type(self):
        """Test if update method raises TypeError when x keyword argument is not an integer."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        """Test if update method raises ValueError when x keyword argument is negative."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-6)

    def test_update_kwargs_invalid_y(self):
        """Test if update method raises TypeError when y keyword argument is not an integer."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        """Test if update method raises ValueError when y keyword argument is negative."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-6)

    def test_update_kwargs_width_before_height(self):
        """Test if update method raises TypeError when width keyword argument is assigned before height."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid", height="invalid")

    def test_update_kwargs_width_before_x(self):
        """Test if update method raises TypeError when width keyword argument is assigned before x."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid", x=1)

    def test_update_kwargs_width_before_y(self):
        """Test if update method raises TypeError when width keyword argument is assigned before y."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="invalid", y=1)

    def test_update_kwargs_height_before_x(self):
        """Test if update method raises TypeError when height keyword argument is assigned before x."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid", x=1)

    def test_update_kwargs_height_before_y(self):
        """Test if update method raises TypeError when height keyword argument is assigned before y."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(height="invalid", y=1)

    def test_update_kwargs_x_before_y(self):
        """Test if update method raises TypeError when x keyword argument is assigned before y."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid", y=1)


class TestRectangleToDictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Rectangle class."""

    def test_to_dictionary(self):
        """Test if to_dictionary method returns the correct dictionary representation."""
        r = Rectangle(10, 10, 10, 10, 10)
        correct = {'id': 10, 'width': 10, 'height': 10, 'x': 10, 'y': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_changed_attributes(self):
        """Test if to_dictionary method returns the correct dictionary representation after changing attributes."""
        r = Rectangle(5, 5, 1, 1, 1)
        r.width = 15
        r.height = 20
        r.x = 5
        r.y = 10
        correct = {'id': 1, 'width': 15, 'height': 20, 'x': 5, 'y': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_args(self):
        """Test if to_dictionary method raises TypeError when called with no arguments."""
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == '__main__':
    unittest.main()
