from database import Database
from exception import ValueNotFoundException, InvalidStatusException, AlreadyHaveEmailException
from generateemails import GenerateEmail

class Controller:

    def __init__(self):
        pass

    def generateemails(self, id):
        database = Database()
        if id not in database:
            raise ValueNotFoundException(id)
        row = database.getrow(id)
        INVALID_STATUS = 'Inativo'
        if row.status == INVALID_STATUS:
            raise InvalidStatusException
        if row.uffmail != '':
            raise AlreadyHaveEmailException
        genemail = GenerateEmail(row.nome)
        return genemail.get_emails_list()

