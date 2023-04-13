''' IMC '''

nome = input('Informe o seu nome: ')
altura = input('Informe a sua altura: ')
peso = input('Informe o seu peso: ')

# altura contain . ou , ?
if ',' in altura:
    altura = altura.replace(',', '.')

if '.' in altura:
    altura = float(altura)
else:
    altura = float(altura) / 100

if ',' in peso:
    peso = peso.replace(',', '.')

print(' Calculando o IMC com peso: ', float(peso), ' e altura: ', float(altura))

# math IMC
imc = float(peso) / (altura * altura)

# print result
print('O IMC de ' + nome + ' é ' + str(imc))