import unittest
from CSVReader.CSVReader import CsvReader, ClassFactory


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('Tests/Data/Data_Statistics_Calc.csv')




if __name__ == '__main__':
    unittest.main()