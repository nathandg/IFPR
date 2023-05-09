altura = input('Informe a sua altura: ')
peso = input('Informe o seu peso: ')
sexo = input('Informe o seu sexo com M ou F:')

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

if sexo == 'M' or sexo == 'm':
    if imc < 20.7:
        print('---> Abaixo do peso')
    elif imc >= 20.7 and imc < 26.4:
        print('---> Peso ideal')
    elif imc >= 26.4 and imc < 27.8:
        print('---> Pouco acima do peso')
    elif imc >= 27.8 and imc < 31.1:
        print('---> Acima do peso ideal')
    elif imc >= 31.1:
        print('---> Obeso')
elif sexo == 'F' or sexo == 'f':
    if imc < 19.1:
        print('---> Abaixo do peso')
    elif imc >= 19.1 and imc < 25.8:
        print('---> Peso ideal')
    elif imc >= 25.8 and imc < 27.3:
        print('---> Pouco acima do peso')
    elif imc >= 27.3 and imc < 32.3:
        print('---> Acima do peso ideal')
    elif imc >= 32.3:
        print('---> Obeso')
else:
    print('Sexo invalido')