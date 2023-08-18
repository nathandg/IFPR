frase = input('Insira sua frase: ')
# frase = 'olha que coisa . mais linda'
print(frase)
frase = frase.lower()
frase = ' ' + frase + ' '

WORDS_COUNT = 0
WHITE_LIST = 'abcdefghijklmnopqrstuvwxyz1234567890éáíóúãõâêôç'

for i, char in enumerate(frase):
    if i > 0 and char != ' ' and frase[i-1] == ' ':
        if char in WHITE_LIST:
            WORDS_COUNT += 1
        else:
            WORDS_COUNT += 1

print('A frase possui', WORDS_COUNT, 'palavras')
