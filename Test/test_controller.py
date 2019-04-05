from unittest import TestCase
from exception import ValueNotFoundException
from controller import Controller


class TestController(TestCase):

    def test_generateemails_invalid_id(self):
        invalidid = 3
        controller = Controller()
        with self.assertRaises(ValueNotFoundException):
            controller.generateemails(invalidid)
