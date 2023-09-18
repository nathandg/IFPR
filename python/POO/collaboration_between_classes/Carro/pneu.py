class Pneu():
  def __init__(self, marca, modelo, tipo, tamanho):
    self.marca = marca
    self.modelo = modelo
    self.tipo = tipo
    self.tamanho = tamanho
  
  def __str__(self):
    return f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Tipo: {self.tipo}
        Tamanho: {self.tamanho}
    """