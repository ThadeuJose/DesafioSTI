class ValueNotFoundException(Exception):
    def __init__(self,id):
        default_message = 'Value {} not found in database'.format(id)
        super().__init__(default_message)