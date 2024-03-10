#!/usr/bin/python3
# 6-max_integer_test.py
'''
 unittests for the function ``def max_integer(list=[]):``
 in the module ``6-max_integer.py``
'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""
    count = [1]

    def tearDown(self):
        print(self.count[0])
        print()
        self.count[0] += 1

    def test_max_integer(self):
        '''basic function use'''
        result = max_integer([1, 2, 3])
        self.assertEqual(result, 3)

    def test_positive_integers(self):
        """Test for positive integers
        """
        pos_int = [1, 2, 3, 4]

        self.assertEqual(max_integer(pos_int), 4)

    def test_negative_integers(self):
        """Test for negative integers
        """
        neg_int = [-33, -77, -3, -5]

        self.assertEqual(max_integer(neg_int), -3)

    def test_mix_integers(self):
        mix_int = [-3, 5, -99, -44, 7, 33]

        self.assertEqual(max_integer(mix_int), 33)

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [33]
        self.assertEqual(max_integer(one_element), 33)

    def test_floats(self):
        """Test a list of floats."""
        floats = [3.33, 9.33, -5.12, 21.33, 7.0]
        self.assertEqual(max_integer(floats), 21.33)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [3.33, 9.33, -3, 7, 6]
        self.assertEqual(max_integer(ints_and_floats), 9.33)

    def test_characters(self):
        """Test for list of characters
        """
        char_list = ['a', 'e', 'm', 'i']
        self.assertEqual(max_integer(char_list), 'm')

    def test_mixed_characters(self):
        """Test for a mixture of characters in list including +ve and -ve
        """
        char_neg = ['-a', '-e', '-m', '-v']
        char_mix = ['-a', '-e', 'm', '-v']

        self.assertEqual(max_integer(char_neg), '-v')
        self.assertEqual(max_integer(char_mix), 'm')

    def test_string(self):
        """Test a string."""
        string = "Dynofin"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Dean", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_none_argument(self):
        """Test for passing None
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_integers_and_strings(self):
        """Test for passing a string in the list
        """
        string_int = [1, 2, 3, 4, "33"]
        with self.assertRaises(TypeError):
            max_integer(string_int)


if __name__ == '__main__':
    unittest.main()
