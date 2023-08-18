number = float(input('Digite o número: '))

def is_par(num):
    ''' Checks if a number is even or odd '''
    if num % 2 == 0:
        print('--> par')
    else:
        print('--> impar')

if number >= 0:
    print('--> positivo')
    is_par(number)
else:
    print('--> negativo')
    is_par(number)
    

    




