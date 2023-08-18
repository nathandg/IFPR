""" Functions to format a phone number """


def recebe_dados():
    """ Recebe o número de telefone do usuário """
    phone_number = input("Digite o número de telefone: ")

    # remove non-digits
    i = 0
    numeric_phone_number = ""
    not_zero = False
    while i < len(phone_number):
        if phone_number[i].isdigit():
            if not_zero:
                numeric_phone_number += phone_number[i]
            elif phone_number[i] != "0":
                not_zero = True
                numeric_phone_number += phone_number[i]
        i += 1

    # device Type
    device_type = ""
    while True:
        device_type = input("Digite o tipo de dispositivo (celular ou fixo): ")
        if device_type in ('celular', 'fixo'):
            break
        print("Tipo de dispositivo inválido, (celular ou fixo)\n")
    return [numeric_phone_number, device_type]


def validacao(data):
    """ Retorna True se o número de telefone for válido """
    # data[0] = phone_number and data[1] = device_type("celular" or "fixo")

    # 43984051115
    if data[1] == "celular":
        if len(data[0]) == 11 and data[0][2] == "9":
            return True
        print("\nCelular deve conter DDD + 9 dígitos iniciando com 9")
        return False

    if data[1] == "fixo":
        if len(data[0]) == 10:
            return True
        print("\nFixo deve conter DDD + 8 dígitos")
        return False
    return False


def formato_internacional(number):
    """ Formata o número de telefone para o formato internacional """
    if len(number) == 10:
        return "+55 " + number[:2] + " " + number[2:6] + "-" + number[6:]

    if len(number) == 11:
        return "+55 " + number[:2] + " " + number[2:7] + "-" + number[7:]

    return None


def formato_interurbano(number):
    """ Formata o número de telefone para o formato interurbano """
    if len(number) == 10:
        return "(" + number[:2] + ") " + number[2:6] + "-" + number[6:]

    if len(number) == 11:
        return "(" + number[:2] + ") " + number[2:7] + "-" + number[7:]

    return None


def formato_ligacao(number):
    """ Formata o número de telefone para o formato de ligação """
    return "0" + number


def print_phone_number(number):
    """ Imprimir as informações do número de telefone """
    print("\n----------------------------")
    print("Formato Internacional: " + formato_internacional(number))
    print("Formato Interurbano: " + formato_interurbano(number))
    print("Formato Ligação: " + formato_ligacao(number))
    print("----------------------------\n")
