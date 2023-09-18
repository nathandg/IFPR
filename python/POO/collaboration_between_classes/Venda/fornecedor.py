class Fornecedor():
    def __init__(self, nome, fone, email, cnpj, endereco):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.cnpj = cnpj
        self.endereco = endereco
    
    def __str__(self):
        return f"""
        Nome: {self.nome}
        Fone: {self.fone}
        Email: {self.email}
        CNPJ: {self.cnpj}
        Endereço: {self.endereco}
        """