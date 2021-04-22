'''
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

def voto(ano):
    from datetime import date # Escopo de importação. Economiza memoria.
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return  f'Com {idade} anos, Não vota.'
    elif 16<= idade < 18 or idade > 65:
        return f'Com {idade} anos, Voto opcional'
    else:
        return  f'Com {idade} anos. Voto Obrigatório'

nasc = int(input('Digite o ano de nascimento'))
print(voto(nasc))
