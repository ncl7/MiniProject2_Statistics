import csv


class CsvReader:

    def __init__(self, filepath):
        data = []
        with open(absolute(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass
