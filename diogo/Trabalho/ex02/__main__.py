""" Desenhos de triângulos e quadrados """


def input_options(options, message):
    """ Função para controlar o input do usuário """
    while True:
        var = input(message)
        if var not in options:
            print("Por favor informe um valor válido.\n")
        else:
            return var


def draw_triangle(length):
    """ Função para desenhar um triângulo """
    i = length
    while i > 0:
      # print("*" * i)
      i -= 1
      
option = input_options(["q", "t"], 'Digite "t' +
                       '" para triangulo ou "q" para quadrado: ')

if option == 't':
    draw_triangle(int(input("Digite o tamanho do triângulo: ")))
