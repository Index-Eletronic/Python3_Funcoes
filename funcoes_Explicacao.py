'''
vamos aprender o que são funções ou rotinas e como utilizar funções em Python. Funções são trechos de código que podem ser
executados em momentos diferentes de nossos códigos em Python.
Veja como funciona o comando def em Python e como utilizá-lo com parâmetros simples e múltiplos.
'''
#=================================================================
def mostreaLinha():
    print('-=' * 30)


mostreaLinha()
print(' SISTEMA DE ALUNOS ')
mostreaLinha()
mostreaLinha()
print(' CADASTRO DE FUNCIONÁRIOS ')
mostreaLinha()
mostreaLinha()
print(' ERRO NO SISTEMA ')
mostreaLinha()
#=================================================================
def texto(txt):
    print('-=' * 30)
    print(txt)
    print('-=' * 30)

    #Programa Principal
texto(' CURSO EM VIDEO ')
texto(' APRENDA PYTHON ')
texto(' FILIPE TUON ')
#=================================================================
def soma(a, b):
    s = a + b
    print(s)

    #Programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)