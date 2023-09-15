"""Introduction to python"""

# Tipos de dados
# int, float, str, bool, list, tuple, dict, set, frozenset, bytes, bytearray, range, complex
IDADE = 30  # int (inteiro)
ALTURA = 1.80  # float (ponto flutuante)
NOME = 'João'  # str (string)
CASADO = False  # bool (True ou False)
filhos = ['Maria', 'José']  # list (permite alteração)
filhos = ('Maria', 'José')  # tuple (não permite alteração)
filhos = {'Maria', 'José'}  # set (não permite duplicidade)

# Funções built-in importantes
# type() --> retorna o tipo de dado
# print() --> imprime na tela
# input() --> recebe dados do usuário
# len() --> retorna o tamanho do dado
# help() --> mostra a documentação do dado
# dir() --> mostra os métodos do dado
# isinstance() --> verifica se o dado é do tipo informado
# id() --> retorna o endereço de memória do dado

# Operadores aritméticos
# +, -, *, /, //, %, **

# Operadores de atribuição
# =, +=, -=, *=, /=, //=, %=, **=

# Operadores de comparação
# ==, !=, >, <, >=, <=

# Operadores lógicos
# and, or, not

# Operadores de identidade
# is, is not

# Operadores de associação
# in, not in

# Operadores ternários
# condição_if_verdadeiro if condição else condição_if_falso

# Estruturas de controle
# if, elif, else
# while
# for
# break
# continue
# pass

# Funções
def function_name():
    """Documentação da função"""
    print('Olá mundo!')

# Funções com parâmetros
def function_parameters(name, age):
    """Escreve o nome e a idade"""
    print(f'Olá {name}! Você tem {age} anos.')

# Funções com parâmetros opcionais
def function_parameters_optional(name, age=0):
    """Escreve o nome e a idade"""
    print(f'Olá {name}! Você tem {age} anos.')

# Funções com retorno
def function_return(name, age):
    """Retorna o nome e a idade"""
    return f'Olá {name}! Você tem {age} anos.'

# how to call a function
function_name()
function_parameters('João', 30)
function_parameters_optional('João')
function_parameters_optional('João', 30)
print(function_return('João', 30))
