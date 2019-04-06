from database import Database
from exception import ValueNotFoundException, InvalidStatusException, AlreadyHaveEmailException
from generateemails import GenerateEmail

class Controller:

    def __init__(self):
        self._database = Database()
        pass

    def generateemails(self, id):
        if id not in self._database:
            raise ValueNotFoundException(id)
        row = self._database.getrow(id)
        INVALID_STATUS = 'Inativo'
        if row.status == INVALID_STATUS:
            raise InvalidStatusException
        if row.uffmail != '':
            raise AlreadyHaveEmailException
        genemail = GenerateEmail(row.nome)
        return genemail.get_emails_list()

    def getfirstname(self, id):
        data = self._database.getrow(id)
        return data.nome.split()[0]

    def getphone(self, id):
        data = self._database.getrow(id)
        return data.telefone

