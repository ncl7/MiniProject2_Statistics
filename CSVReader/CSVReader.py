import csv
from Fileutilities.absolutepath import absolutepath


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:

    def __init__(self, filepath):
        self.data = []

        with open(absolutepath(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)

        pass
