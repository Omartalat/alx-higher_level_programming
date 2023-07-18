#!/usr/bin/python3
"""
Defines unittests for base.py.
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unit tests for testing instantiation of the Base class."""

    def test_no_arg(self):
        """
        Test case to ensure that two instances of the Base class
        created without any arguments have consecutive id values.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """
        Test case to verify that three instances of the Base class
        have consecutive id values.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        """
        Test case to check if two instances of the Base class created
        with None as an argument have consecutive id values.
        """
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """
        Test case to validate that an instance of the Base class created
        with a unique id value returns the same id value.
        """
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        """
        Test case to verify the number of instances created
        after an instance of the Base class with a unique id.
        """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        """
        Test case to check if the id attribute of
        an instance of the Base class can be modified.
        """
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        """
        Test case to confirm that accessing the __nb_instances
        attribute of the Base class raises an AttributeError.
        """
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        """
        Test case to validate that the id attribute of an instance of
        the Base class created with a string argument is the same
        as the input string.
        """
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        """
        Test case to verify that the id attribute of an instance of
        the Base class created with a float argument is
        the same as the input float.
        """
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        """
        Test case to ensure that the id attribute of an instance of
        the Base class created with a complex number argument is
        the same as the input complex number.
        """
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        """
        Test case to validate that the id attribute of an instance of
        the Base class created with a dictionary argument is the same
        as the input dictionary.
        """
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        """
        Test case to verify that the id attribute of an instance of
        the Base class created with a boolean argument is the same
        as the input boolean.
        """
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        """
        Test case to check if the id attribute of an instance of
        the Base class created with a list argument is the same
        as the input list.
        """
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        """
        Test case to validate that the id attribute of an instance of
        the Base class created with a tuple argument is the same
        as the input tuple.
        """
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        """
        Test case to ensure that the id attribute of an instance of
        the Base class created with a set argument is the same
        as the input set.
        """
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        """
        Test case to verify that the id attribute of an instance of the
        Base class created with a frozenset argument is the same
        as the input frozenset.
        """
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        """
        Test case to check if the id attribute of an instance of the
        Base class created with a range argument is the same
        as the input range.
        """
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        """
        Test case to validate that the id attribute of an instance of the
        Base class created with a bytes argument is the same
        as the input bytes.
        """
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        """
        Test case to ensure that the id attribute of an instance of the
        Base class created with a bytearray argument is the same
        as the input bytearray.
        """
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        """
        Test case to verify that the id attribute of an instance of the
        Base class created with a memoryview argument is the same
        as the input memoryview.
        """
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        """
        Test case to check if the id attribute of an instance of the
        Base class created with float('inf')
        as an argument is infinity.
        """
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        """
        Test case to validate that the id attribute of
        an instance of the Base class created with float('nan')
        as an argument is not a number.
        """
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        """
        Test case to ensure that creating an instance of the
        Base class with two arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_instantiation(unittest.TestCase):
    """
    Unit tests for testing instantiation of the Base class.
    """

    def test_no_arg(self):
        """
        Test case to ensure that two instances of the Base class created
        without any arguments have consecutive id values.
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """
        Test case to verify that three instances of the
        Base class have consecutive id values.
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        """
        Test case to check if two instances of the Base
        class created with None as an argument have consecutive id values.
        """
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """
        Test case to validate that an instance of the Base
        class created with a unique id value returns the same id value.
        """
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        """
        Test case to verify the number of instances created after
        an instance of the Base class with a unique id.
        """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        """
        Test case to check if the id attribute of an instance of
        the Base class can be modified.
        """
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        """
        Test case to confirm that accessing the __nb_instances attribute
        of the Base class raises an AttributeError.
        """
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        """
        Test case to validate that the id attribute of an instance of the
        Base class created with a string argument is the same
        as the input string.
        """
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        """
        Test case to verify that the id attribute of an instance of the Base class created with a float argument is the same as the input float.
        """
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        """
        Test case to ensure that the id attribute of an instance of the Base class created with a complex number argument is the same as the input complex number.
        """
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        """
        Test case to validate that the id attribute of an instance of the Base class created with a dictionary argument is the same as the input dictionary.
        """
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        """
        Test case to verify that the id attribute of an instance of the Base class created with a boolean argument is the same as the input boolean.
        """
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        """
        Test case to check if the id attribute of an instance of the Base class created with a list argument is the same as the input list.
        """
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        """
        Test case to validate that the id attribute of an instance of the Base class created with a tuple argument is the same as the input tuple.
        """
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        """
        Test case to ensure that the id attribute of an instance of the Base class created with a set argument is the same as the input set.
        """
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        """
        Test case to verify that the id attribute of an instance of the Base class created with a frozenset argument is the same as the input frozenset.
        """
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        """
        Test case to check if the id attribute of an instance of the Base class created with a range argument is the same as the input range.
        """
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        """
        Test case to validate that the id attribute of an instance of the Base class created with a bytes argument is the same as the input bytes.
        """
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        """
        Test case to ensure that the id attribute of an instance of the Base class created with a bytearray argument is the same as the input bytearray.
        """
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        """
        Test case to verify that the id attribute of an instance of the Base class created with a memoryview argument is the same as the input memoryview.
        """
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        """
        Test case to check if the id attribute of an instance of the Base class created with float('inf') as an argument is infinity.
        """
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        """
        Test case to validate that the id attribute of an instance of the Base class created with float('nan') as an argument is not a number.
        """
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        """
        Test case to ensure that creating an instance of the Base class with two arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_save_to_file(unittest.TestCase):
    """Unit tests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """
        Clean up by deleting any created files.
        """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        """
        Test case to ensure that the save_to_file method saves a single Rectangle object to a file and the file size is correct.
        """
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        """
        Test case to verify that the save_to_file method saves a list of two Rectangle objects to a file and the file size is correct.
        """
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        """
        Test case to ensure that the save_to_file method saves a single Square object to a file and the file size is correct.
        """
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        """
        Test case to verify that the save_to_file method saves a list of two Square objects to a file and the file size is correct.
        """
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        """
        Test case to check if the save_to_file method uses the class name as the filename when called with a single object of a derived class.
        """
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        """
        Test case to ensure that the save_to_file method overwrites the existing file when called multiple times with the same filename.
        """
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        """
        Test case to check if the save_to_file method saves an empty list as '[]' when called with None.
        """
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        """
        Test case to ensure that the save_to_file method saves an empty list as '[]' when called with an empty list.
        """
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        """
        Test case to confirm that calling save_to_file method without any arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        """
        Test case to check if calling save_to_file method with more than one argument raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        """
        Test case to ensure that the from_json_string method returns a list when called with a valid JSON string.
        """
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        """
        Test case to verify that the from_json_string method correctly converts a JSON string to a list of Rectangle objects.
        """
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        """
        Test case to ensure that the from_json_string method correctly converts a JSON string to a list of Rectangle objects when called with multiple rectangles.
        """
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        """
        Test case to ensure that the from_json_string method correctly converts a JSON string to a list of Square objects.
        """
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        """
        Test case to verify that the from_json_string method correctly converts a JSON string to a list of Square objects when called with multiple squares.
        """
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        """
        Test case to check if the from_json_string method returns an empty list when called with None.
        """
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        """
        Test case to ensure that the from_json_string method returns an empty list when called with an empty JSON list string.
        """
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """
        Test case to confirm that calling from_json_string method without any arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        """
        Test case to check if calling from_json_string method with more than one argument raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        """
        Test case to verify that the create method correctly creates a Rectangle object from a dictionary.
        """
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        """
        Test case to ensure that the create method creates a new Rectangle object and not a reference to the original object.
        """
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        """
        Test case to check if the create method creates a new Rectangle object and not the same object.
        """
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        """
        Test case to ensure that the create method creates a new Rectangle object with the same attributes but not equal to the original object.
        """
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        """
        Test case to verify that the create method correctly creates a Square object from a dictionary.
        """
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        """
        Test case to ensure that the create method creates a new Square object and not a reference to the original object.
        """
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        """
        Test case to check if the create method creates a new Square object and not the same object.
        """
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        """
        Test case to ensure that the create method creates a new Square object with the same attributes but not equal to the original object.
        """
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file method of Base class."""

    @classmethod
    def tearDown(self):
        """
        Clean up by deleting any created files.
        """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        """
        Test case to ensure that the load_from_file method loads the first Rectangle object correctly from the file.
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        """
        Test case to verify that the load_from_file method loads the second Rectangle object correctly from the file.
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        """
        Test case to ensure that the load_from_file method returns a list of Rectangle objects.
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        """
        Test case to ensure that the load_from_file method loads the first Square object correctly from the file.
        """
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        """
        Test case to verify that the load_from_file method loads the second Square object correctly from the file.
        """
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        """
        Test case to ensure that the load_from_file method returns a list of Square objects.
        """
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        """
        Test case to check if the load_from_file method returns an empty list when the file does not exist.
        """
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        """
        Test case to check if calling load_from_file method with more than one argument raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """
        Clean up by deleting any created files.
        """
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        """
        Test case to ensure that the save_to_file_csv method saves a single Rectangle object to a CSV file.
        """
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        """
        Test case to verify that the save_to_file_csv method saves a list of two Rectangle objects to a CSV file.
        """
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        """
        Test case to ensure that the save_to_file_csv method saves a single Square object to a CSV file.
        """
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        """
        Test case to verify that the save_to_file_csv method saves a list of two Square objects to a CSV file.
        """
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        """
        Test case to check if the save_to_file_csv method uses the class name as the filename when called with a single object of a derived class.
        """
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        """
        Test case to verify that the save_to_file_csv method overwrites the content of the CSV file when called multiple times.
        """
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        """
        Test case to ensure that the save_to_file_csv method saves an empty list as "[]" when called with None.
        """
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        """
        Test case to ensure that the save_to_file_csv method saves an empty list as "[]" when called with an empty list.
        """
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        """
        Test case to confirm that calling save_to_file_csv method without any arguments raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        """
        Test case to check if calling save_to_file_csv method with more than one argument raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """
        Clean up by deleting any created files.
        """
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        """
        Test case to ensure that the load_from_file_csv method loads the first Rectangle object correctly from the CSV file.
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        """
        Test case to verify that the load_from_file_csv method loads the second Rectangle object correctly from the CSV file.
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        """
        Test case to ensure that the load_from_file_csv method returns a list of Rectangle objects.
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        """
        Test case to ensure that the load_from_file_csv method loads the first Square object correctly from the CSV file.
        """
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        """
        Test case to verify that the load_from_file_csv method loads the second Square object correctly from the CSV file.
        """
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        """
        Test case to ensure that the load_from_file_csv method returns a list of Square objects.
        """
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_no_file(self):
        """
        Test case to check if the load_from_file_csv method returns an empty list when the file does not exist.
        """
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        """
        Test case to check if calling load_from_file_csv method with more than one argument raises a TypeError.
        """
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
