from pessoas.pessoa import Pessoa

class Vendedor(Pessoa):
    def __init__(self, nome, fone, email, comissao, cpf, endereco):
        super().__init__(nome, endereco, fone, email)
        self.comissao = comissao
        self.cpf = cpf
    
    def __str__(self):
        return f"""
        Nome: {self.nome}
        Fone: {self.fone}
        Email: {self.email}
        Comissão: {self.comissao}
        CPF: {self.cpf}
        Endereço: {self.endereco}
        """