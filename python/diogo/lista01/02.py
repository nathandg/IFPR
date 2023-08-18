''' Exercício 02 '''

QUANTIDADE_NOTAS = 4
notas = []

def maior_nota(notas):
    """ return the biggest note """
    maior = notas[0]
    for i in range(len(notas)):
        maior = notas[i] if maior <= notas[i] else maior
    return maior

def menor_nota(notas):
    """ return the smallest note """
    menor = notas[0]
    for i in range(len(notas)):
        menor = notas[i] if menor >= notas[i] else menor
    return menor

def calculaMedia(notas):
    """ return the average of notes """
    soma = 0
    for i in range(len(notas)):
        soma += notas[i]
    return soma / len(notas)

def notas_iguais(notas):
    """ returna as notas iguais """
    notasIguais = []
    for i in range(len(notas)):
        isEqual = 0
        for j in range(len(notas)):
            if notas[i] == notas[j]:
                isEqual+=1
        if isEqual >= 2:
            notasIguais.append(i+1)
            isEqual = False
    return notasIguais

def resultado_final(mediaFinal):
    if mediaFinal <= 4:
        return 'Reprovado'
    elif mediaFinal < 7:
        return 'Recuperação'
    elif mediaFinal < 8:
        return 'Aprovado'
    elif mediaFinal < 9:
        return 'Aprovado com ótimo desempenho'
    elif mediaFinal <= 10:
        return 'Aprovado com desempenho excelente'
    else:
        return 'Reprovado, média final invalida'

# obtain the notes
for i in range(QUANTIDADE_NOTAS):
    notas.append(float(input("Digite a nota " + str(i + 1) + ": ")))

media = calculaMedia(notas)
print('\n ----- Resultado -----')
print('Notas são:', notas)
print('Maior nota é:', maior_nota(notas))
print('Menor nota é:', menor_nota(notas))
print('Média das notas é:', media)
notasIguais = notas_iguais(notas)
if (len(notasIguais) > 0):
    print('Notas iguais: ', notasIguais)
else:
    print('Não há notas iguais')
print('Aluno está ' + resultado_final(media))
print(' ---------------------\n')