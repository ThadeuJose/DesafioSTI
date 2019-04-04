import csv
from row import Row


class Database:

    def __init__(self):

        filename = 'alunos.csv'
        mode = 'r'

        with open(filename, mode) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            self.csv_list = []
            for row in csv_reader:
                self.csv_list.append(Row(row))

    def __str__(self):
        resp = ''
        for line_count, row in enumerate(self.csv_list):
            resp += "{} {}\n".format(line_count+1, row)
        return resp