import unittest

from Statistics.Statistics import Statistics
from CSVReader.CSVReader import CsvReader
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    #def test_zscore(self):
    #    test_data = CsvReader(# Enter file path for test data here).data


if __name__ == '__main__':
    unittest.main()
