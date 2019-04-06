from controller import Controller
from exception import ValueNotFoundException, InvalidStatusException, AlreadyHaveEmailException


class View:

    def __init__(self):
        self.controller = Controller()
        self.initialprompt()

    def initialprompt(self):
        print('Digite sua matrícula:')
        mat = input()
        try:
            salutation = '{}, por favor escolha uma das opções abaixo para o seu UFFMail:'
            print(salutation.format(self.controller.getfirstname(mat)))
            emails = self.controller.generateemails(mat)
            for idx, el in enumerate(emails):
                print('{} - {}'.format(idx+1, el))
            try:
                idx = int(input())
                max_available = len(emails)
                if not 1 < idx < max_available:
                    raise ValueError
                message = 'A criação de seu e-mail ({email}) será feita nos próximos minutos.\n' \
                          'Um SMS foi enviado para {phone} com a sua senha de acesso.'
                print(message.format(email=emails[idx - 1], phone=self.controller.getphone(mat)))
            except ValueError:
                print('Por favor, na próxima vez digite um número válido de 1 a {}'.format(max_available))
        except ValueNotFoundException:
            print('Matrícula não encontrada')
        except InvalidStatusException:
            print('Você se encontra inativo por isso não pode ter um uffmail.')
        except AlreadyHaveEmailException:
            print('Você já tem um uffmail por isso não pode fazer um novo uffmail.')







