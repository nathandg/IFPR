from pessoas.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, fone, email, cpf, endereco):
      super().__init__(nome, endereco, fone, email)
      self.cpf = cpf
    
    def __str__(self):
        return f"""
        Nome: {self.nome}
        Fone: {self.fone}
        Email: {self.email}
        CPF: {self.cpf}
        Endereço: {self.endereco}
        """