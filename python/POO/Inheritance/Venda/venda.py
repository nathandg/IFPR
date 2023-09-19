from parcela import Parcela

class Venda():
    def __init__(self, data, totalVenda, numeroNotaFiscal, cliente, vendedor, qtdParcelas):
        self.data = data
        self.totalVenda = totalVenda
        self.numeroNotaFiscal = numeroNotaFiscal
        self.cliente = cliente
        self.vendedor = vendedor
        self.qtdParcelas = qtdParcelas
        self.parcelas = self.calcularParcelas()
    
    def calcularParcelas(self):
        parcelas = []
        valor = self.totalVenda / self.qtdParcelas
        for i in range(self.qtdParcelas):
            data = self.data.split("/")
            
            data[1] = int(data[1]) + i
            if data[1] > 12:
                data[1] = data[1] - 12
                data[2] = int(data[2]) + 1
            
            new_data = f"{data[0]}/{data[1]}/{data[2]}"
            
            parcela = Parcela(new_data, i+1, False)
            parcelas.append(parcela)
            
        return parcelas
    
    def __str__(self):
      parcelas_str = "\n".join([str(parcela) for parcela in self.parcelas])
      return f"""
        Data: {self.data}
        Total da Venda: {self.totalVenda}
        Número da Nota Fiscal: {self.numeroNotaFiscal}
        Cliente: {self.cliente}
        Vendedor: {self.vendedor}
        Quantidade de Parcelas: {self.qtdParcelas}
        Parcelas: {parcelas_str}
      """
