'''
Funcoes teoria 2
'''
# Interactive HELP - Ajuda interativa - help()
#ex:
help(print())
print(input.__doc__)

# docstrings = Documento
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

# Parametros Opcionais
