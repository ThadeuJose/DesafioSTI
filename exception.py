class ValueNotFoundException(Exception):
    def __init__(self, id):
        default_message = 'Value {} not found in database'.format(id)
        super().__init__(default_message)


class InvalidStatusException(Exception):
    def __init__(self):
        default_message = 'Student is Inactive'
        super().__init__(default_message)

class AlreadyHaveEmailException(Exception):
    def __init__(self):
        default_message = 'Student already have a Uffmail'
        super().__init__(default_message)