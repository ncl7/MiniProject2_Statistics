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
        for row in test_result:
            self.assertEqual(self.statistics.pop_mean(test_data), float(row['Population Mean (Female)']))
            # self.assertEqual(self.statistics.result, test_result['Population Mean (Female)'])

    def test_median(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.med(test_data), float(row['Median']))
            # self.assertEqual(self.statistics.result, float(row['Median']))

    def test_mode(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.mod(test_data), float(row['Mode']))
            # self.assertEqual(self.statistics.result, test_result(row['Mode']))

    def test_population_stand_deviation(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.population_st_dev(test_data), float(row['Population SD (Female)']))
            # self.assertEqual(self.statistics.result, test_result(row['Population SD (Female)']))

    def test_var_pop_proportion(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.variance_pop_proportion(test_data), float(row['Var Population Prop']))
            #self.assertEqual(self.statistics.result, test_result(row['Var Population Prop']))

    def test_proportion(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.proportion(test_data), float(row['Proportion']))
            #self.assertEqual(self.statistics.result, test_result(row['Proportion']))

    def test_sample_mean(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.sample_mean(test_data), float(row['Sample Mean']))
            #self.assertEqual(self.statistics.result, test_result(row['Sample Mean']))

    def test_sample_st_dev(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.sample_st_dev(test_data), float(row['Sample SD']))
            #self.assertEqual(self.statistics.result, test_result(row['Sample SD']))

    def test_sample_var_prop(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.var_sam_prop(test_data), float(row['Variance of Sample Proportion']))
            #self.assertEqual(self.statistics.result, test_result(row['Variance of Sample Proportion']))

    def test_p_value(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.p_value(test_data), float(row['P Value']))
            #self.assertEqual(self.statistics.result, test_result(row['P Value']))

    def test_z_score(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.z_score(test_data), float(row['ZScore']))
            #self.assertEqual(self.statistics.result, test_result(row['ZScore']))

    def test_confidence_interval(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.confidence_interval(test_data[0]),
                             float(row['Confidence Interval (Lower)']))
            self.assertEqual(self.statistics.confidence_interval(test_data[1]),
                             float(row['Confidence Interval (Upper)']))
            self.assertEqual(self.statistics.result, test_result(row['Confidence Interval (Lower)'], row['Confidence '
                                                                                                         'Interval ('
                                                                                                         'Upper)']))

    def test_population_variance(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv').data
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.population_variance(test_data), float(row['Population Variance']))
            #self.assertEqual(self.statistics.result, test_result(row['Population Variance']))

    def test_pop_correlation_coefficient(self):
        test_data = CsvReaderStats('Tests/Data/female_height.csv')
        test_result = CsvReader('Tests/Data/Results_Statistics_Calc.csv').data
        for row in test_result:
            self.assertEqual(self.statistics.pop_correlation_coefficient(test_data),
                             float(row['Population '
                                       'Correlation '
                                       'Coefficient']))
            #self.assertEqual(self.statistics.result, test_result(row['Population Correlation Coefficient']))


if __name__ == '__main__':
    unittest.main()
