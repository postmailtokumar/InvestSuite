import unittest
import find_length


class TestStringMethods(unittest.TestCase):

    def test_integer(self):
        inp = 123
        val_res = find_length.validate_input(inp)
        if val_res is not None:
            result = find_length.find_len(val_res)
            self.assertEqual(result, 3)

    def test_float(self):
        inp = 34.5
        val_res = find_length.validate_input(inp)
        if val_res is not None:
            result = find_length.find_len(val_res)
            self.assertEqual(result, 2)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
