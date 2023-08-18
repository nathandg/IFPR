""" phone number input """
import phone_formatter as pf

while True:
    input_data = pf.recebe_dados()
    VALID_NUMBER = pf.validacao(input_data)

    if VALID_NUMBER:
        pf.print_phone_number(input_data[0])
    else:
        print("Número de telefone inválido\n")
