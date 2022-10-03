#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_(unittest.TestCase):
    """Define unittests for rectangle"""
    def test_rectangle_isinstance_base(self):
        """Test if Rectangle is an instance of Base"""
        self.assertIsInstance(Rectangle(13, 9), Base)

    def test_rectangle_with_no_args(self):
        """testing with no argument in rectangle()"""
        with self.assertRaises(TypeError):
            print(Rectangle())

    def test_rectangle_with_one_args(self):
        """testing with only one argument in rectangle()"""
        with self.assertRaises(TypeError):
            print(Rectangle(10))

    def test_rectangle_with_two_args(self):
        """Test with two arguments"""
        rec1 = Rectangle(8, 18)
        rec2 = Rectangle(12, 9)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_multiple_rectangle(self):
        """Test with two arguments"""
        rec1 = Rectangle(8, 18)
        rec2 = Rectangle(12, 9)
        self.assertEqual(rec1.id, 1)
        self.assertEqual(rec2.id, 2)

    def test_rectangle_with_three_args(self):
        """Test with three arguments"""
        rec1 = Rectangle(8, 18, 2)
        rec2 = Rectangle(12, 9, 3)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_rectangle_with_four_args(self):
        """Test with four arguments"""
        rec1 = Rectangle(8, 18, 2, 1)
        rec2 = Rectangle(12, 9, 3, 2)
        self.assertEqual(rec1.id, rec2.id - 1)

    def test_with_five_args(self):
        """Test with five arguments"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.id, 2)

    def test_with_morethan_five_args(self):
        """Test with more than five arguments"""
        with self.assertRaises(TypeError):
            print(Rectangle(8, 18, 2, 0, 2, 6).id)

    def test_private_width(self):
        """Test width as a private instance attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 18, 2, 0, 2).__width)

    def test_private_height(self):
        """Test height as a private instance attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 18, 2, 0, 2).__height)
    
    def test_private_x(self):
        """Test x as a private instance attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 18, 2, 0, 2).__x)
    
    def test_private_y(self):
        """Test y as a private instance attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 18, 2, 0, 2).__y)
    
    def test_private_id(self):
        """Test id as a private instance attribute"""
        with self.assertRaises(AttributeError):
            print(Rectangle(8, 18, 2, 0, 2).__id)

    def test_id_getter(self):
        """Test gettin id"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.id, 2)

    def test_id_setter(self):
        """Test setting id"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.id = 3
        self.assertEqual(rec1.id, 3)

class TestRectangle_width(unittest.TestCase):
    def test_width_getter(self):
        """Test gettin width"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.width, 8)

    def test_width_setter(self):
        """Test setting width"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.width = 10
        self.assertEqual(rec1.width, 10)

    def test_width_as_None(self):
        """Test width as None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(None, 2, 3, 2).width)

    def test_width_as_float(self):
        """Test width as float"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(3.8, 18, 2, 0, 2).width)

    def test_width_as_string(self):
        """Test width as string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle("hey", 18, 2, 0, 2).width)

    def test_width_as_zero(self):
        """Test width as zero"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            print(Rectangle(0, 18, 2, 0, 2).width)

    def test_width_as_negative(self):
        """Test width as negative value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            print(Rectangle(-5, 18, 2, 0, 2).width)

    def test_width_as_bool(self):
        """Test width as bool"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(True, 18, 2, 0, 2).width)

    def test_width_as_complex(self):
        """Test width as complex"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(complex(5), 18, 2, 0, 2).width)

    def test_width_as_inf(self):
        """Test width as inf"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(float('inf'), 18, 2, 0, 2).width)
    
    def test_width_as_NaN(self):
        """Test width as NaN"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(float('NaN'), 18, 2, 0, 2).width)
    
    def test_width_as_list(self):
        """Test width as list"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle([10], 18, 2, 0, 2).width)

    def test_width_as_set(self):
        """Test width as set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle({10}, 18, 2, 0, 2).width)

    def test_width_as_dict(self):
        """Test width as dictionary"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle({'name': 'ade', 'age': 10}, 18, 2, 0, 2).width)
    
    def test_width_as_tupple(self):
        """Test width as tupple"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle((1, 2, 5), 18, 2, 0, 2).width)

    def test_width_as_byte(self):
        """Test width as byte"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(b'baboon', 18, 2, 0, 2).width)

    def test_width_as_frozenSet(self):
        """Test width as frozen set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(frozenset({1, 2, 3}), 18, 2, 0, 2).width)

class TestRectangle_height(unittest.TestCase):
    def test_height_getter(self):
        """Test getting height"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.height, 18)

    def test_height_setter(self):
        """Test settin height"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.height = 12
        self.assertEqual(rec1.height, 12)

    def test_heigt_as_float(self):
        """Test height as float"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, 4.8, 2, 0, 2).height)

    def test_height_as_string(self):
        """Test height as string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, "hey", 2, 0, 2).height)

    def test_height_as_zero(self):
        """Test height as zero"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            print(Rectangle(18, 0, 2, 0, 2).height)

    def test_height_as_complex(self):
        """Test height as complex value"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, complex(7), 2, 0, 2).height)

    def test_height_as_None(self):
        """Test height as None"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(1, None, 3, 0).height)

    def test_height_as_negative(self):
        """Test height as negative value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            print(Rectangle(18, -5, 2, 0, 2).height)

    def test_height_as_bool(self):
        """Test height as bool"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, True, 2, 0, 2).height)

    def test_height_as_inf(self):
        """Test height as inf"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, float('inf'), 2, 0, 2).height)
    
    def test_height_as_NaN(self):
        """Test height as NaN"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, float('NaN'), 2, 0, 2).height)
    
    def test_height_as_list(self):
        """Test height as list"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, [10], 2, 0, 2).height)

    def test_height_as_set(self):
        """Test height as set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, {10}, 2, 0, 2).height)

    def test_height_as_dict(self):
        """Test height as dictionary"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, {'name': 'ade', 'age': 10}, 2, 0, 2).height)
    
    def test_height_as_tupple(self):
        """Test height as tupple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, (1, 2, 5), 2, 0, 2).y)

    def test_height_as_byte(self):
        """Test height as byte"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, b'baboon', 2, 0, 2).height)

    def test_height_as_frozenSet(self):
        """Test height as frozen set"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, frozenset({1, 2, 3}), 2, 0, 2).height)

class TestRectangle_x(unittest.TestCase):
    def test_x_getter(self):
        """Test getting x"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.x, 2)
    
    def test_x_setter(self):
        """Test setting x"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.x = 3
        self.assertEqual(rec1.x, 3)

    def test_x_as_zero(self):
        """Test x as zero"""
        rec1 = Rectangle(8, 18, 0, 2, 2)
        self.assertEqual(rec1.x, 0)
    
    def test_x_as_None(self):
        """Test x as None"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(1, 2, None, 2).x)

    def test_x_as_complex(self):
        """Test x as complex"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, 10, 2j, 0, 2).x)

    def test_x_as_float(self):
        """Test x as float"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, 20, 4.8, 2).x)

    def test_x_as_string(self):
        """Test x as string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, 2, "hey", 2, 1).x)

    def test_x_as_negative(self):
        """Test x as negative value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            print(Rectangle(10, 9, -5, 0, 2).x)

    def test_x_as_bool(self):
        """Test x as bool"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(10, 8, True, 0, 2).x)

    def test_x_as_inf(self):
        """Test x as inf"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(10, 7,  float('inf'), 2, 1).x)
    
    def test_x_as_NaN(self):
        """Test x as NaN"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(11, 6, float('NaN'), 2, 2).x)
    
    def test_x_as_list(self):
        """Test x as list"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(12, 8, [10], 0, 2).x)

    def test_x_as_set(self):
        """Test x as set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(12, 8, {3}, 0, 2).x)
    
    def test_x_as_dict(self):
        """Test x as dictionary"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, 2, {'name': 'ade', 'age': 10}, 0, 2).x)
    
    def test_x_as_tupple(self):
        """Test x as tupple"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(18, 2, (1, 2, 5), 0, 2).x)

    def test_x_as_byte(self):
        """Test x as byte"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(12, 8, b'tired', 0, 2).x)

    def test_x_as_frozenSet(self):
        """Test x as frozen set"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(9, 12, frozenset({1, 2, 3}), 0, 2).x)

class TestRectangle_y(unittest.TestCase):
    def test_y_getter(self):
        """Test gettin y"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.y, 0)

    def test_y_setter(self):
        """Test setting y"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        rec1.y = 1
        self.assertEqual(rec1.y, 1)

    def test_y_as_zero(self):
        """Test y as zero"""
        rec1 = Rectangle(8, 18, 2, 0, 2)
        self.assertEqual(rec1.y, 0)

    def test_y_as_None(self):
        """Test y as None"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(1, 2, 3, None).y)

    def test_y_as_complex(self):
        """Test y as complex"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(18, 2, 2, 2j, 1).y)

    def test_y_as_float(self):
        """Test y as float"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(18, 20, 2, 4.8).y)

    def test_y_as_string(self):
        """Test y as string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(18, 2, 2, "hey", 1).y)

    def test_y_as_negative(self):
        """Test y as negative value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            print(Rectangle(10, 9, 0, -5, 2).y)

    def test_y_as_bool(self):
        """Test y as bool"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(10, 8, 0, True, 2).y)

    def test_y_as_inf(self):
        """Test y as inf"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(10, 7, 2, float('inf'), 1).y)
    
    def test_y_as_NaN(self):
        """Test y as NaN"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(11, 6, 2, float('NaN'), 2).y)
    
    def test_y_as_list(self):
        """Test y as list"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(12, 8, 0, [10], 2).y)

    def test_y_as_set(self):
        """Test y as set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(12, 8, 0, {3}, 2).y)

    def test_y_as_dict(self):
        """Test y as dictionary"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(18, 2, 0, {'name': 'ade', 'age': 10}, 2).y)
    
    def test_y_as_tupple(self):
        """Test y as tupple"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(18, 2, 0, (1, 2, 5), 2).y)

    def test_y_as_byte(self):
        """Test y as byte"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(12, 8, 0, b'tired', 2).y)

    def test_y_as_frozenSet(self):
        """Test y as frozen set"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            print(Rectangle(9, 12, 0, frozenset({1, 2, 3}), 2).y)
    
class TestRectangle_order_of_initiation(unittest.TestCase):
    def test_width_before_height(self):
        """Test width as None"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(None, 12j, 3, 2).width)

    def test_width_before_x(self):
        """Test width as set"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle({10}, 18, True, 0, 2).width)
    
    def test_width_before_y(self):
        """Test width as byte"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            print(Rectangle(b'baboon', 18, 2, [10], 2).width)

    def test_height_before_x(self):
        """Test height as tupple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, (1, 2, 5), True, 0, 2).y)

    def test_height_before_y(self):
        """Test height as tupple"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            print(Rectangle(18, (1, 2, 5), 10, {1}, 2).y)

    def test_x_before_y(self):
        """Test x as byte"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            print(Rectangle(12, 8, b'tired', 1j, 2).x)

class TestRectangle_area(unittest.TestCase):
    """testing the area method of the Rectangle class."""

    def test_area(self):
        """Testing area"""
        rec = Rectangle(18, 2, 0, 1, 2)
        self.assertEqual(rec1.area(), 36)
    
    def test_area_with_longInt(self):
        """Testing area"""
        rec = Rectangle(99988889788888, 888888667598767, 1, 2)
        self.assertEqual(rec.area(), 88878991019124613304519101096)

    def test_area(self):
        """Testing area"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.width = 10
        rec.height = 13
        self.assertEqual(rec1.area(), 130)

    def test_area(self):
        """Testing area with parameter"""
        with self.assertRaises(TypeError):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.area(1))

class TestRectangle_Display(unittest.TestCase):
    def test_display_no_arg(self):
        """testing display function with no arguments"""
        with self.assertRaises(TypeError):
            Rectangle().display()

    def test_display_one_arg(self):
        """testing display function with one arguments"""
        with self.assertRaises(TypeError):
            Rectangle(2).display()

    def test_display_one_str_arg(self):
        """testing display function with one int arguments"""
        with self.assertRaises(TypeError):
            Rectangle("hey").display()
    
    def test_display_two_str_arg(self):
        """testing display function with two int arguments"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hey", "hi").display()

    def test_display_oneStr_oneInt_arg(self):
        """testing display function with 1 int and 1 str arguments"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("hey", 3).display()


class TestRectangle_str_(unittest.TestCase):
    def test_str_no_arg(self):
        """testing __str__ function with no arguments"""
        with self.assertRaises(TypeError):
            r =Rectangle()
            print(r.__str__())

    def test_str_one_arg(self):
        """testing __str__ function with 1 arguments"""
        with self.assertRaises(TypeError):
            r =Rectangle(10)
            print(r.__str__())
    
    def test_str_one_arg(self):
        """testing __str__ function with 1 arguments"""
        with self.assertRaises(TypeError):
            r =Rectangle("hey")
            print(r.__str__())
    
    def test_str_two_arg(self):
        """testing __str__ function with 2 arguments"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r =Rectangle("hey", 10)
            print(r.__str__())
    
    def test_str_three_arg(self):
        """testing __str__ function with 3 arguments"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r =Rectangle(11, "hey", 1)
            print(r.__str__())
    
    def test_str_five_arg(self):
        """testing __str__ function with 5 arguments"""
        rec = Rectangle(10, 6, 3, 2, 2)
        print(rec.__str__())
        self.assertEqual(str(rec), "[Rectangle] (2) 3/2 - 10/6")
    
    def test_str_five_arg(self):
        """testing __str__ function with 5 arguments"""
        rec = Rectangle(10, 6, 3, 2, "hi")
        print(rec.__str__())
        self.assertEqual(str(rec), "[Rectangle] (hi) 3/2 - 10/6")

    def test_str_six_arg(self):
        """testing __str__ function with 4 arguments"""
        with self.assertRaises(TypeError):
            rec = Rectangle(10, 6, 3, 2, 1, 2)
            print(rec.__str__())
        
class TestRectangle_update(unittest.TestCase):
    def test_update_no_arg(self):
        """testing update function with no arguments"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update()
        self.assertEqual(str(rec), "[Rectangle] (2) 0/1 - 18/2")

    def test_update_arg_withNone(self):
        """testing update function with None"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(None)
        self.assertEqual(str(rec), "[Rectangle] (None) 0/1 - 18/2")

    def test_update_one_arg(self):
        """testing update function with 1 argument"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(10)
        self.assertEqual(str(rec), "[Rectangle] (10) 0/1 - 18/2")

    def test_update_two_arg(self):
        """testing update function with 2 arguments"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(10, 5)
        self.assertEqual(str(rec), "[Rectangle] (10) 0/1 - 5/2")
    
    def test_update_three_arg(self):
        """testing update function with 3 arguments"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(10, 5, 9)
        self.assertEqual(str(rec), "[Rectangle] (10) 0/1 - 5/9")
    
    def test_update_four_arg(self):
        """testing update function with 4 arguments"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(10, 5, 9, 2)
        self.assertEqual(str(rec), "[Rectangle] (10) 2/1 - 5/9")
    
    def test_update_five_arg(self):
        """testing update function with 5 arguments"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(10, 5, 9, 2, 1)
        self.assertEqual(str(rec), "[Rectangle] (10) 2/1 - 5/9")
        
    def test_update_more_than_five_arg(self):
        """testing update function with more than 5 arguments"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(10, 5, 9, 2, 1, 5)
        self.assertEqual(str(rec), "[Rectangle] (10) 2/1 - 5/9")

    def test_update_args_twice(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(18, 2, 10, 1, 2, 20)
        rec.update(16, 15, 8, 2, 3, 9)
        self.assertEqual("[Rectangle] (16) 2/3 - 15/8", str(rec))

    def test_update_arg(self):
        """testing update args with width as string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, "hey", 3, 4))

    def test_update_arg(self):
        """testing update args with width as 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, 0, 3, 4))

    def test_update_arg_negativeWidth(self):
        """testing update args with width as negative"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, -3, 3, 4))

    def test_update_args_height(self):
        """testing update with height as string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, 10, "hey", 3, 4))

    def test_update_args_zeroHeight(self):
        """testing update args with height as 0"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, 10, 0, 3, 4))

    def test_update_args_negativeHeight(self):
        """testing update args with height as negative"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, 10, -10, 3, 4))

    def test_update_args_string_x(self):
        """testing update with x as string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, 10, 9, "3", 4))
    
    def test_update_args_negativeX(self):
        """testing update with x as negative"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, 10, 9, -2, 4))

    def test_update_args_stringY(self):
        """testing update with y as string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, 10, 8, 3, "4"))
    
    def test_update_args_negativeY(self):
        """testing update with y as negative"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, 10, 8, 3, -4))
        
    def test_update_arg_width_beforeHeight(self):
        """testing update args with width before height"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, "hey", -3, 4, 2))

    def test_update_arg_width_beforeX(self):
        """testing update args with width before x"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, "hey", 3, True, 2))

    def test_update_arg_width_beforeY(self):
        """testing update args with width before x"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, True, 3, 2, float('inf')))

    def test_update_arg_height_beforeX(self):
        """testing update args with height before x"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, 10, {'name': "ade", 'age': 23}, -2, 1))

    def test_update_arg_height_beforeY(self):
        """testing update args with height before x"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, 10, float('NaN'), 2, float('inf')))
    
    def test_update_arg_x_beforeY(self):
        """testing update args with width before x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(1, 10, 13, {10}, 2))
    

class TestRectangle_update_kwargs(unittest.TestCase):
    """testing update kwargs of Rectangle class."""
    def test_update_kwargs_one(self):
        """testing kwargs with one arg"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(id=1)
        self.assertEqual(str(rec), "[Rectangle] (1) 0/1 - 18/2")

    def test_update_two_kwarg(self):
        """testing update kwargs function with 2 arguments"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(id=10, width=5)
        self.assertEqual(str(rec), "[Rectangle] (10) 0/1 - 5/2")
    
    def test_update_three_kwarg(self):
        """testing update kwargs function with 3 arguments"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(id=10, height=9, width=5)
        self.assertEqual(str(rec), "[Rectangle] (10) 0/1 - 5/9")
    
    def test_update_four_kwarg(self):
        """testing update kwargs function with 4 arguments"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(width=5, x=2, id=10, height=9)
        self.assertEqual(str(rec), "[Rectangle] (10) 2/1 - 5/9")

    def test_update_five_arg(self):
        """testing update function with 5 arguments"""
        rec = Rectangle(18, 2, 0, 1, 2)
        rec.update(y=1, width=5, id=10, x=2, height=9)
        self.assertEqual(str(rec), "[Rectangle] (10) 2/1 - 5/9")
    
    def test_update_kwargs_with_more_values(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=16, width=15, y=3, x=2, height=8, z=9)
        self.assertEqual("[Rectangle] (16) 2/3 - 15/8", str(rec))
    
    def test_update_kwargs_twice(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=18, width=2, height=10, y=2, x=1)
        rec.update(id=16, width=15, y=3, x=2, height=8)
        self.assertEqual("[Rectangle] (16) 2/3 - 15/8", str(rec))

    def test_update_kwargs(self):
        """testing update kwargs with width as string"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(id=1, width="hey", height=3, x=4))
        
    def test_update_kwargs(self):
        """testing update kwargs with width as 0"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(x=1, width=0, height=3, y=4))

    def test_update_arg_negativeWidth(self):
        """testing update kwargs with width as negative"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(id=1, width=-3, y=3, height=4))

    def test_update_kwargs_height(self):
        """testing update kwargs with height as string"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(id=1, height="hey", width=3))

    def test_update_kwargs_zeroHeight(self):
        """testing update kwargs with height as 0"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(width=1, height=0, y=3))

    def test_update_kwargs_negativeHeight(self):
        """testing update kwargs with height as negative"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(height=-10))

    def test_update_args_string_x(self):
        """testing update with x as string"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(y=1, height=10, width=9, x="3", id=4))
    
    def test_update_args_negativeX(self):
        """testing update with x as negative"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(width=10, height=9, x=-2, y=4))

    def test_update_args_stringY(self):
        """testing update with y as string"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(id=10, height=8, width=3, y="4"))
    
    def test_update_args_negativeY(self):
        """testing update with y as negative"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec = Rectangle(18, 2, 0, 1, 2)
            print(rec.update(height=8, width=3, y=-4))

class TestRectangle_dictionary(unittest.TestCase):
    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        print(r.to_dictionary())
        self.assertEqual(str(rec), {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9})

    def test_to_dictionary(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, 9, 5)
            print(r.to_dictionary(1))