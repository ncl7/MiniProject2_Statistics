import unittest
from CSVReader.CSVReader import CsvReader
from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)
        
    def test_pop_mean(self):
        test_data = CsvReader("Tests/Data/female_height.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.pop_mean())

    def test_z_score(self):
        test_data = CsvReader("Tests/Data/female_height.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.z_score())

if __name__ == '__main__':
    unittest.main()
