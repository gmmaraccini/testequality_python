import math
import random

valor_original = input('Digite o valor a ser sacado -> ')
qtd_notas = int(input('Digite a quantidade de notas diferentes  -> '))
notas = []
for i in range(qtd_notas):
    x = int(input('Digite o valor da nota '))
    notas.append(x)

def separar_notas(notas,valor_original) :
    valor_temp = float(valor_original)
    separacao_notas = ""
    for nota in notas:
        int(nota)
        valor = (valor_temp/nota)
        valor_temp = (valor_temp%nota)
        if math.floor(valor) != 0:
            separacao_notas += "\nSao necessarias " + str(math.floor(valor)) + " notas de R$ " + str(nota)

    if valor_temp > 0:
        print('ERRO - NAO TEM NOTA SUFICIENTE PARA ESTE VALOR')
    else:
        print(separacao_notas)


print('\nPrimeira Sequencia :')
random.shuffle(notas)
separar_notas(notas, valor_original)
print('\nSegunda Sequencia :')
notas.sort(reverse=True)
separar_notas(notas, valor_original)
print('\nTerceira Sequencia :')
notas.sort()
separar_notas(notas, valor_original)
