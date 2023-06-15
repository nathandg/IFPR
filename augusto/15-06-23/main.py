""" Main file for the project """

import my_lib as ml

print(" Escolha a opção desejada: ")
print("\t 1 - Calcular a área de um círculo")
print("\t 2 - Calcular o perímetro de um círculo")
print('\t 3 - Calcular a área de um quadrado')
print('\t 4 - Calcular o perímetro de um quadrado')
print('\t 5 - Sair')

while True:
    option = input("\n Digite a opção desejada: ")
    if option == '1':
        radius = float(input("\n Informe o raio do círculo: "))
        print("A área é ", ml.math_area_of_circle(radius))
    elif option == '2':
        radius = float(input("\n Informe o raio do círculo: "))
        print("O perímetro é ", ml.math_perimeter_of_circle(radius))
    elif option == '3':
        side = float(input("\n Informe o lado do quadrado: "))
        print("A área é ", ml.math_area_of_square(side))
    elif option == '4':
        side = float(input("\n Informe o lado do quadrado: "))
        print("O perímetro é ", ml.math_perimeter_of_square(side))
    elif option == '5':
        print("Saindo...")
        break
