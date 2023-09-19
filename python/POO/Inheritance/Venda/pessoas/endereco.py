class Endereco():
    def __init__(self, logradouro, numero, complemento, bairro, cep, cidade, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"""
          Logradouro: {self.logradouro} 
          Número: {self.numero}
          Complemento: {self.complemento}
          Bairro: {self.bairro}
          CEP: {self.cep}
          Cidade: {self.cidade}
          Estado: {self.estado}
        """
