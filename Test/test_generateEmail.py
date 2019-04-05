from unittest import TestCase
from generateemails import GenerateEmail

class TestGenerateEmail(TestCase):
    def setUp(self):
        name = "Laura Azevedo Cunha"
        self.generateemail = GenerateEmail(name)

    '''
    1 - laura_azevedo@id.uff.br
    2 - lauraac@id.uff.br
    3 - lauracunha@id.uff.br
    4 - lcunha@id.uff.br
    5 - lazevedocunha@id.uff.br    
    '''

    def test__generate_by_first_second_name(self):
        self.assertEqual('laura_azevedo', self.generateemail._generate_by_first_second_name())

    def test__generate_by_first_name_initial_letters(self):
        self.assertEqual('lauraac', self.generateemail._generate_by_first_name_initial_letters())

    def test__generate_by_first_last_name(self):
        self.assertEqual('lauracunha', self.generateemail._generate_by_first_last_name())

    def test__generate_by_first_letter_and_last_name(self):
        self.assertEqual('lcunha', self.generateemail._generate_by_first_letter_and_last_name())

    def test__generate_by_initial_letter_and_others_names(self):
        self.assertEqual('lazevedocunha', self.generateemail._generate_by_initial_letter_and_others_names())

    def test_get_emails_list(self):
        #Ordena as duas listas e checa se elas são iguais
        list1 = sorted(self.generateemail.get_emails_list())
        list2 = sorted(['laura_azevedo@id.uff.br', 'lauraac@id.uff.br', 'lauracunha@id.uff.br',
                        'lcunha@id.uff.br', 'lazevedocunha@id.uff.br'])
        isEqual = True
        for i, k in zip(list1, list2):
            if i != k:
                isEqual = False
        self.assertTrue(isEqual)
