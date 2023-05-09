number = int(input("Enter a number: "))

if number % 2 == 0:
    print("--> par")
else:
    print("--> impar")

if number > 0:
    print("--> positivo")
elif number < 0:
    print("--> negativo")
else:
    print("--> zero")

if number % 3 == 0:
    print("--> multiplo de 3")
elif number % 5 == 0:
    print("--> multiplo de 5")
