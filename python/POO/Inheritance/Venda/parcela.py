class Parcela():
    def __init__(self, dataVencimento, parcela, pago):
        self.dataVencimento = dataVencimento
        self.parcela = parcela
        self.pago = pago
    
    def __str__(self):
        return f"""
            Data de Vencimento: {self.dataVencimento}
            Parcela: {self.parcela}
            Pago: {self.pago}
        """