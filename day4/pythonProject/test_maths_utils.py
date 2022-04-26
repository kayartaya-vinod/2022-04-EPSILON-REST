import unittest
import maths_utils


class TestMathsUtils(unittest.TestCase):

    def test_add_two_ints(self):
        actual = maths_utils.calculate_sum('10, 20')
        expected = 30
        self.assertEqual(actual, expected)

    def test_add_two_floats(self):
        actual = maths_utils.calculate_sum('10.2, 20.2')
        expected = 30.4
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
