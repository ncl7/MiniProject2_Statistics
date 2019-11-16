import unittest
from CSVReader.CSVReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_reader = CsvReader('Tests/Data/female_height.csv')

    def test_csvreader(self):
        function = []
        test = len(self.csv_reader.data)
        for test in function:
            self.assertEqual(self.csv_reader.data)


if __name__ == '__main__':
    unittest.main()
