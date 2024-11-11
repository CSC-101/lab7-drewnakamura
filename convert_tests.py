import unittest

import convert


class TestCases(unittest.TestCase):
    def test_str_to_float(self):
        string = "1.02"
        self.assertEqual(1.02, convert.string_to_float(string))

    def test_str_to_float_2(self):
        string = "helo"
        self.assertEqual(None, convert.string_to_float(string))

