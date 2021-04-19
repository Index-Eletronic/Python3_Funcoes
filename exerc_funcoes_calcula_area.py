'''
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''

def area(larg, comp):
    a = larg * comp
    print(f' A Area de um terreno com {larg} e comprimento {comp} é de {a}mq')

 #Programa Principal.
l = float(input('Digite a largura'))
c = float(input('Digite o comprimento'))
area(l, c)