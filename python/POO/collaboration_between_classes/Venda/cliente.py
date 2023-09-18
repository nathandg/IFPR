class Cliente():
    def __init__(self, nome, fone, email, cpf, endereco):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.cpf = cpf
        self.endereco = endereco
    
    def __str__(self):
        return f"""
        Nome: {self.nome}
        Fone: {self.fone}
        Email: {self.email}
        CPF: {self.cpf}
        Endereço: {self.endereco}
        """