class Vendedor():
    def __init__(self, nome, fone, email, comissao, cpf, endereco):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.comissao = comissao
        self.cpf = cpf
        self.endereco = endereco
    
    def __str__(self):
        return f"""
        Nome: {self.nome}
        Fone: {self.fone}
        Email: {self.email}
        Comissão: {self.comissao}
        CPF: {self.cpf}
        Endereço: {self.endereco}
        """