'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
 O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

def fecha(jog='<Desconhecido>', gol=0):
    print(f'Jogador {jog} fez {gol} gol(s) no campeonato')



n = str(input('Nome do Jogado: '))
g = int(input('Numero de gols'))
if g.isnumeric(): # Se g for numerico
    g = int(g)  # Então g recebe o int de g
else:
    g = 0
if n.strip() == '': # Se passar o nome vazio
    ficha(gol=g)# recebe so a quantidade de gols
else:
    ficha(n, g)# Se nao, jog=n e g=gol
