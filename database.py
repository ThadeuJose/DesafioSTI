import csv
from row import Row
from exception import ValueNotFoundException


class Database:

    def __init__(self):
        filename = 'alunos.csv'
        mode = 'r'

        with open(filename, mode) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            self.csv_list = []
            for row in csv_reader:
                self.csv_list.append(Row(row))

    def getrow(self, id):
        for row in self.csv_list:
            if row.matricula == id:
                return row
        raise ValueNotFoundException(id)

    def __contains__(self, id):
        for row in self.csv_list:
            if row.matricula == id:
                return True
        return False

    def __str__(self):
        resp = ''
        for line_count, row in enumerate(self.csv_list):
            resp += "{} {}\n".format(line_count+1, row)
        return resp
