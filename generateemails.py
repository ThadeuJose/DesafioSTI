class GenerateEmail:

    def __init__(self, name):
        self.names = name.lower().split()

        local_part_list = []

        for generator in self._get_all_generators():
            local_part = self._call_generator(generator)
            local_part_list.append(local_part)

        self._list = list(map(self._concatWithIdUff, local_part_list))

    def _get_all_generators(self):
        return [method for method in dir(self) if callable(getattr(self, method)) if method.startswith('_generate')]

    def _call_generator(self, generator):
        return getattr(self, generator)()

    def _concatWithIdUff(self, alias):
        return "{}@id.uff.br".format(alias)

    '''
    1 - laura_azevedo@id.uff.br
    2 - lauraac@id.uff.br
    3 - lauracunha@id.uff.br
    4 - lcunha@id.uff.br
    5 - lazevedocunha@id.uff.br
    '''
    def _generate_by_first_second_name(self):
        first_name = self.names[0]
        second_name = self.names[1]
        return '{}_{}'.format(first_name, second_name)

    def _generate_by_first_name_initial_letters(self):
        first_name = self.names[0]
        initial_letters = ''
        for name in self.names[1:]:
            initial_letters += name[0]
        return '{}{}'.format(first_name, initial_letters)

    def _generate_by_first_last_name(self):
        first_name = self.names[0]
        last_name = self.names[-1]
        return '{}{}'.format(first_name, last_name)

    def _generate_by_first_letter_and_last_name(self):
        firstletter = self.names[0][0]
        lastname = self.names[-1]
        return "{}{}".format(firstletter, lastname)

    def _generate_by_initial_letter_and_others_names(self):
        initial_letter = self.names[0][0]
        other_names = ''
        for name in self.names[1:]:
            other_names += name
        return '{}{}'.format(initial_letter, other_names)

    def get_emails_list(self):
        return self._list