import unittest
from CSVReader.CSVReader import CsvReader
from Statistics.Statistics import Statistics
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)
        
    def test_pop_mean(self):
        test_data = CsvReader('Tests/Data/Data_Statistics_Calc.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.pop_mean())
            self.assertEqual(self.statistics.result, ())

    def test_proportion(self):
        test_data = CsvReader('Tests/Data/Data_Statistics_Calc.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.proportion(test_data(['Height'])))
            self.assertEqual(self.statistics.result, test_result(row['Proportion']))

    def test_sample_mean(self):
        test_data = CsvReader('Tests/Data/Data_Statistics_Calc.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.sample_mean(test_data(['Height'])))
            self.assertEqual(self.statistics.result, test_result(row['Sample Mean']))

    def test_sample_st_dev(self):
        test_data = CsvReader('Tests/Data/Data_Statistics_Calc.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.sample_st_dev(test_data(['Height'])))
            self.assertEqual(self.statistics.result, test_result(row['Sample SD']))

    def test_sample_var_prop(self):
        test_data = CsvReader('Tests/Data/Data_Statistics_Calc.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.var_sam_prop(test_data(['Height'])))
            self.assertEqual(self.statistics.result, test_result(row['Variance of Sample Proportion']))

    def test_p_value(self):
        test_data = CsvReader('Tests/Data/Data_Statistics_Calc.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        pprint(test_data)
        pprint(test_result)
        for row in test_data:
            self.assertEqual(self.statistics.p_value(test_data(['Height'])))
            self.assertEqual(self.statistics.result, test_result(row['P Value']))


    def test_z_score(self):
        test_data = CsvReader("Tests/Data/female_height.csv").data
        for row in test_data:
            self.assertEqual(self.statistics.z_score())

if __name__ == '__main__':
    unittest.main()
