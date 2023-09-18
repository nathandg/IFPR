from endereco import Endereco

from vendedor import Vendedor
from cliente import Cliente
from fornecedor import Fornecedor
from venda import Venda

endereco = Endereco(
  "Rua das Flores",
  "123",
  "Apto 101",
  "Centro",
  "12345-000",
  "São Paulo",
  "SP"
)

vendedor = Vendedor(
  "João da Silva",
  "(11) 99999-9999",
  "joao@ifpr.com",
  560,
  "000.000.000-00",
  endereco
)

cliente = Cliente(
  "Maria da Silva",
  "(11) 99999-9999",
  "maria@ifpr.com",
  "000.000.000-00",
  endereco
)

fornecedor = Fornecedor(
  "Lojas AA",
  "(11) 99999-9999",
  "suporte@lojasa.com",
  "00.000.000/0000-00",
  endereco
)

print(vendedor)
print(cliente)
print(fornecedor)

print(" ---- Realizando Venda ---- ")
venda = Venda(
  "17/11/2023",
  3000.00,
  12356564,
  cliente,
  vendedor,
  3,
)

print(venda)