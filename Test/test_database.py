from unittest import TestCase
from database import Database
from exception import ValueNotFoundException
from row import Row

class TestDatabase(TestCase):
    def setUp(self):
        self.invalidid = "3"
        self.validid = "100591"
        self.database = Database()

    def test___contains__validid(self):
        self.assertTrue(self.validid in self.database)

    def test_not__contains__invalidid(self):
        self.assertFalse(self.invalidid in self.database)

    def test_get_valid_row(self):
        dictrow = dict()
        dictrow['nome'] = 'Lucas Oliveira Barros'
        dictrow['matricula'] = '100591'
        dictrow['telefone'] = '99999-9980'
        dictrow['email'] = "email@gmail.com"
        dictrow['uffmail'] = ""
        dictrow['status'] = "Ativo"

        row = Row(dictrow)

        self.assertEqual(row, self.database.getrow(self.validid))


    def test_get_invalid_row(self):
        with self.assertRaises(ValueNotFoundException):
            self.database.getrow(self.invalidid)