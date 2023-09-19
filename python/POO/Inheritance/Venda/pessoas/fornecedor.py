from pessoas.pessoa import Pessoa

class Fornecedor(Pessoa):
    def __init__(self, nome, fone, email, cnpj, endereco):
      super().__init__(nome, endereco, fone, email)
      self.cnpj = cnpj
          
    def __str__(self):
        return f"""
        Nome: {self.nome}
        Fone: {self.fone}
        Email: {self.email}
        CNPJ: {self.cnpj}
        Endereço: {self.endereco}
        """