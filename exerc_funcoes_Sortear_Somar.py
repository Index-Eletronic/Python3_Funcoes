'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint

def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(1, 100))
        print(f'Sorteando os valores de uma lista {cont}')

#def somaPar():


numeros = list()
sorteia(numeros)
