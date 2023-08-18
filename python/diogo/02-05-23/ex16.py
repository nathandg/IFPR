import os 
print("\t Welcome to the unit converter !")

while True:
    print('Select one option: ')
    print('1 - Convert m/s to km/h')
    print('2 - Convert milha/h to Km/s')
    print('3 - Convert Km/h to nos')
    print('4 - Convert m/h em nos pes/s')
    print('0 - Exit \n')

    try :
        option = int(input())
        if option == 1:
            print('Insert a value in m/s, to convert to km/h: ')
            ms = float(input())
            print('The value in km/h is: ', ms * 3.6)
        elif option == 2:
            print('Insert a value in milha/h, to convert to Km/s: ')
            mh = float(input())
            print('The value in km/s is: ', mh * 1.609)
        elif option == 3:
            print('Insert a value in km/h, to convert to nos: ')
            kmh = float(input())
            print('The value in nos is: ', kmh / 1.852)
        elif option == 4:
            print('Insert a value in m/h, to convert to pes/s: ')
            mh = float(input())
            print('The value in nos is: ', mh / 1097)
        elif option == 0:
            print('Exiting...')
            break
    except ValueError:
        print(str(os.system('cls' if os.name == 'nt' else 'clear')) + 'pa insira os dados corretamente!\n')
        print('Invalid value, try again !\n')
        continue
