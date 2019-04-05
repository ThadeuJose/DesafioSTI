from database import Database
from exception import ValueNotFoundException


class Controller:

    '''
    def generateEmails(id):
        database = Database()

        if id not in database:
            raise Exception
        row = database.getRow(id)
        INVALID_STATUS = 'Inativo'
        if row.status == INVALID_STATUS:
            raise Exception
        if row.email != '':
            raise Exception
        generateListByName(row.nome)

    getEmails('105798')
    '''
    def __init__(self):
        pass

    def generateemails(self, id):
        database = Database()
        if id not in database:
            raise ValueNotFoundException(id)
        row = database.getrow(id)
