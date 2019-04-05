from unittest import TestCase
from exception import ValueNotFoundException, InvalidStatusException
from controller import Controller


class TestController(TestCase):

    def setUp(self):
        self.invalid_id = "3"
        self.inactive_id = "106447"
        self.controller = Controller()

    def test_generateemails_invalid_id(self):
        with self.assertRaises(ValueNotFoundException):
            self.controller.generateemails(self.invalid_id)


    def test_generateemails_inactive_id(self):
        with self.assertRaises(InvalidStatusException):
            self.controller.generateemails(self.inactive_id)
