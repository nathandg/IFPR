""" Calculo de dosagem """
print("\t Calculo de dosagem")

def input_options(options, message):
    """ Função para controlar o input do usuário """
    while True:
        var = input(message)
        if var not in options:
            print("Por favor informe um valor válido.\n")
        else:
            return var

diabetico = input_options(['s','n'], 'Possui diabetes: [s, n] ')
gestante = input_options(['s', 'n'], 'Está grávida: [s, n] ')
sexo = input_options(['m', 'f'], 'Sexo: [m, f] ')


while True:
    idade = input("Idade: [anos] ")
    if idade.isnumeric():
        idade = int(idade)
        break
    else:
        print("A idade deve ser um número inteiro.\n")

while True:
    peso = input("Peso: [kg]")
    try:
        peso = float(peso)
        break
    except ValueError:
        print("Informe um valor válido.\n")

while True:
    temperatura = input("Temperatura: [ºC] ")
    try:
        temperatura = float(temperatura)
        break
    except ValueError:
        print("Informe um valor válido.\n")

if diabetico == 's' or gestante == 's' or idade < 7:
    print("\nRemédio não recomendado.")
elif sexo == 'f':
    print('\n\tCalculando dosagem para mulher\n')
    if 37 < temperatura <= 37.9:
        if idade >= 18:
            print("Dosagem: ", peso / 4, ' gotas')
        else:
            print("Dosagem: ", peso / 6, ' gotas')
    elif 38 < temperatura <= 39.9:
        if idade >= 18:
            print("Dosagem: ", peso / 3, ' gotas')
        else:
            print("Dosagem: ", peso / 4, ' gotas')
    elif temperatura >= 40:
        if idade >= 18:
            print("Dosagem: ", peso / 2, ' gotas')
        else:
            print("Dosagem: ", peso / 3, ' gotas')
elif sexo == 'm':
    print('\n\tCalculando dosagem para homem\n')
    if 37 < temperatura <= 37.9:
        if idade >= 18:
            print("Dosagem: ", peso / 4, ' gotas')
        else:
            print("Dosagem: ", peso / 5, ' gotas')
    elif 38 < temperatura <= 39.9:
        if idade >= 18:
            print("Dosagem: ", peso / 3, ' gotas')
        else:
            print("Dosagem: ", peso / 4, ' gotas')
    elif temperatura >= 40:
        if idade >= 18:
            print("Dosagem: ", peso / 1, ' gotas')
        else:
            print("Dosagem: ", peso / 2, ' gotas')
 