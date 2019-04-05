class Row:
    def __init__(self, row):
        self.nome = row['nome']
        self.matricula = row['matricula']
        self.telefone = row['telefone']
        self.email = row['email']
        self.uffmail = row['uffmail']
        self.status = row['status']

    def __eq__(self, other):
        return self.matricula == other.matricula

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.nome, self.matricula, self.telefone, self.email, self.uffmail, self.status)