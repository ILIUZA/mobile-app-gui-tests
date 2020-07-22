import csv
import sys


def getDataFromFile(file_name):
    """
    :param file_name: a file with data for test case
    :return: data(list) with rows from a file except the first row
    """
    data = []
    with open(file_name, encoding="utf8") as f:
        reader = csv.reader(f, delimiter=';')
        next(f)  # skip the first row
        try:
            for row in reader:
                data.append(row)
        except csv.Error as e:
            sys.exit('File {}, line {}: {}'.format(file_name, reader.line_num, e))
    return data
