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

    def test_add_numbers_with_strings(self):
        actual = maths_utils.calculate_sum('10.2, 20.2, vinod, False, 10')
        expected = 40.4
        self.assertEqual(actual, expected)

    def test_raise_value_error_for_number_input(self):
        try:
            maths_utils.calculate_sum(123)
            self.fail('Expected ValueError to be raised. But did not receive any!')
        except ValueError:
            # test passes; nothing to be done her
            pass

    def test_raise_value_error_for_bool_input(self):
        with self.assertRaises(ValueError):
            maths_utils.calculate_sum(False)


if __name__ == '__main__':
    unittest.main()
