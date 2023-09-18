class Carro():
  def __init__(self, marca, modelo, cor, p1, p2, p3, p4):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.p1 = p1
    self.p2 = p2
    self.p3 = p3
    self.p4 = p4
  
  def __str__(self):
    return f"""
        Carro
    Marca: {self.marca}
    Modelo: {self.modelo}
    Cor: {self.cor}
    Pneu 1: {self.p1}
    Pneu 2: {self.p2}
    Pneu 3: {self.p3}
    Pneu 4: {self.p4}
    """