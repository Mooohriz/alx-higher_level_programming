#!/usr/bin/python3
"""Unittests for base."""
import os
import pep8
import unittest
from models.base import Base


class TestPep8(unittest.TestCase):
    """Pep8 models/base.py & tests/test_models/test_base.py"""
    def test_pep8(self):
        """Pep8"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        files = ["models/base.py", "tests/test_models/test_base.py"]
        errors += style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

class TestBase(unittest.TestCase):
    """Define unittests for base"""

    def test_base_with_no_args(self):
        """Test without a value for id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
    
    def test_base_with_one_arg(self):
        """Test with a value for id"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
    
    def test_multiple_bases(self):
        """Test without a value for id multiple times"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_multiple_bases(self):
        """Test without a value for id multiple times"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)

    def test_base_with_str(self):
        """Test with a string for id"""
        b1 = Base("hey")
        self.assertEqual(b1.id, hey)

    def test_base_with_str(self):
        """Test with a bool value for id"""
        b1 = Base(True)
        self.assertEqual(b1.id, True)

    def test_base_with_one_floatArg(self):
        """Test with a float value for id"""
        b1 = Base(3.9)
        self.assertEqual(b1.id, 3.9)

    def test_base_with_list(self):
        """Test with a list value for id"""
        b1 = Base([1, "hello", 4])
        self.assertEqual(b1.id, [1, "hello", 4])

    def test_base_with_set(self):
        """Test with a list value for id"""
        b1 = Base({1, "hello", 4})
        self.assertEqual(b1.id, {1, "hello", 4})

    def test_base_with_dict(self):
        """Test with a dictionary value for id"""
        b1 = Base({'num': 1, 'name': "hello", 'age': 4})
        self.assertEqual(b1.id, {'num': 1, 'name': "hello", 'age': 4})

    def test_base_with_frozenSet(self):
        """Test with a frozen set value for id"""
        self.assertEqual((Base(frozenset({1, 2, 3})).id), frozenset({1, 2, 3}))

    def test_base_with_tuple(self):
        """Test with a tuple value for id"""
        self.assertEqual(Base((1, "hey", 20)).id, (1, "hey", 20))

    def test_base_with_nan(self):
        """Test with a NaN for id"""
        self.assertNotEqual(Base(float('nan')).id, float('nan'))

    def test_base_with_inf(self):
        """Test with a inf for id"""
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_base_with_byte(self):
        """Test with a byte datatype for id"""
        self.assertEqual(Base(b'basket').id, b'basket')

    def test_base_with_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

if __name__ == "__main__":
    unittest.main()
