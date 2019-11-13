import unittest
from CSVReader.CSVReader import CsvReader
from CSVReader.CSVStatsReader import CsvReaderStats
from Statistics.Statistics import Statistics
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_pop_mean(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        pprint(test_data)
        for row in test_result:
            self.assertEqual(self.statistics.pop_mean(test_data), float(row['Population Mean (Female)']))
            self.assertEqual(self.statistics.result, test_result['Population Mean (Female)'])

    def test_median(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.statistics.med(test_data), float(row['Median']))
            self.assertEqual(self.statistics.result, float(row['Median']))

    def test_mode(self):
        test_data = CsvReader('Tests/Data/female_data.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.mod(), float(row['Mode']))
            self.assertEqual(self.statistics.result, test_result(row['Mode']))

    def test_population_stand_deviation(self):
        test_data = CsvReader('Tests/Data/female_data.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.population_st_dev(), float(row['Population SD (Female)']))
            self.assertEqual(self.statistics.result, test_result(row['Population SD (Female)']))

    def test_var_pop_proportion(self):
        test_data = CsvReader('Tests/Data/female_data.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.population_st_dev(), float(row['Population SD (Female)']))
            self.assertEqual(self.statistics.result, test_result(row['Population SD (Female)']))

    def test_proportion(self):
        test_data = CsvReader('Tests/Data/female_data.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.proportion(), float(row['Proportion']))
            self.assertEqual(self.statistics.result, test_result(row['Proportion']))

    def test_sample_mean(self):
        test_data = CsvReader('Tests/Data/female_data.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.sample_mean(), float(row['Sample Mean']))
            self.assertEqual(self.statistics.result, test_result(row['Sample Mean']))

    def test_sample_st_dev(self):
        test_data = CsvReader('Tests/Data/female_data.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.sample_st_dev(), float(row['Sample SD']))
            self.assertEqual(self.statistics.result, test_result(row['Sample SD']))

    def test_sample_var_prop(self):
        test_data = CsvReader('Tests/Data/female_data.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.var_sam_prop(), float(row['Variance of Sample Proportion']))
            self.assertEqual(self.statistics.result, test_result(row['Variance of Sample Proportion']))

    def test_p_value(self):
        test_data = CsvReader('Tests/Data/female_data.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.p_value(), float(row['P Value']))
            self.assertEqual(self.statistics.result, test_result(row['P Value']))

    def test_z_score(self):
        test_data = CsvReader('Tests/Data/female_data.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_data:
            self.assertEqual(self.statistics.z_score(), float(row['ZScore']))
            self.assertEqual(self.statistics.result, test_result(row['ZScore']))


if __name__ == '__main__':
    unittest.main()
