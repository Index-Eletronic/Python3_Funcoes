'''
Funcoes teoria 2
'''
# Interactive HELP - Ajuda interativa - help()
#ex:
help(print())
print(input.__doc__)

#=============================docstrings = Documento
def contador(i, f, p):
   """
   ASPAS DUPLAS = docstrings ou manual.
   :param i:
   :param f:
   :param p:
   :return:
   """
    c=i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')

# =============================Parametros Opcionais
def somar(a=0, b=0, c=0): # Quando NÃO tiver parametro, passa a valer 0.
    s= a + b + c
    print(f'A soma vale {s}')


somar(3,2,5)
somar(8.4)

#================================Escopo de variaveis

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = soma(3,2,5)
r2 = soma(1,7)
r3 = soma(4)
