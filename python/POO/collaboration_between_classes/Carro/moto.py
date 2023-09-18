class Moto():
  def __init__(self, marca, modelo, cor, p1, p2):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.p1 = p1
    self.p2 = p2
  
  def __str__(self):
    return f"""
        Moto
    Marca: {self.marca}
    Modelo: {self.modelo}
    Cor: {self.cor}
    Pneu 1: {self.p1}
    Pneu 2: {self.p2}
    """