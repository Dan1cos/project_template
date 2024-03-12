import unittest
import pandas as pd
from app.io.input import file_input, pandas_input


class TestInputFile(unittest.TestCase):

    def test_input(self):
        self.assertEqual(file_input("test_input_string.txt"), "Hello, I'm string")
        self.assertEqual(file_input("test_input.txt"), "name,age\nArtem,20\nRoman,14\nMax,20")

    def test_input_error(self):
        self.assertRaises(FileNotFoundError, file_input, "unknown.txt")

    def test_input_empty(self):
        self.assertTrue(len(file_input("empty_input.txt")) == 0)

    def test_input_pandas_frames(self):
        df = pd.DataFrame([["Artem", 20], ["Roman", 14], ["Max", 20]], columns=["name", "age"])
        pd.testing.assert_frame_equal(pandas_input("test_input.txt"), df)

    def test_input_pandas_indexes(self):
        index = pd.Index([0, 1, 2])
        pd.testing.assert_index_equal(pandas_input("test_input.txt").index, index)

    def test_input_pandas_error(self):
        self.assertRaises(FileNotFoundError, pandas_input, "unknown.txt")