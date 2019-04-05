from unittest import TestCase
from database import Database


class TestDatabase(TestCase):
    def setUp(self):
        self.invalidid = "3"
        self.validid = "100591"
        self.database = Database()

    def test___contains__validid(self):
        self.assertTrue(self.validid in self.database)

    def test_not__contains__invalidid(self):
        self.assertFalse(self.invalidid in self.database)