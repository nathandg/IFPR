import turtle

print('Informe os lados do triangulo: ')

try:
    l1 = float(input('Lado 1: '))
    l2 = float(input('Lado 2: '))
    l3 = float(input('Lado 3: '))
except ValueError:
    print('Invalid value, please insert a number !')
    exit()

if l1 == l2 and l2 == l3:
    # this is a equilateral triangle because all sides are equal
    print('Triangulo equilatero \n')

elif l1 == l2 or l2 == l3 or l1 == l3:
    # this is a isosceles triangle because two sides are equal
    print('Triangulo isosceles \n')
else:
    # this is a scalene triangle because all sides are different
    print('Triangulo escaleno \n')

altura = int(l1)
base_esquerda = int(l2)
base_direita = int(l3)

for linha in range(altura):
    if linha == 0:
        print(' '*(base_direita-1)+'^')
    elif linha < altura-1:
        print(' '*(base_direita-linha-1)+'/'+' '*(linha+linha+base_esquerda-4)+'\\')
    else:
        print('<'+'-'*(base_esquerda+base_direita-3)+'>')