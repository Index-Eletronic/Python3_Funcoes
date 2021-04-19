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
# pode fazer também soma(a=4, b=5)
soma(8, 9)
# pode fazer também soma(b=4, a=5)
soma(2, 1)

#==================================================================
def soma(a, b):
    print(f'A = {a} e B={b}')
    s= a + b
    print(f'A soma de A + B = {s}')

# Programa Principal:
soma(4, 5)
#=================== EMPACOTAR PARAMETROS - TUPLAS ============================
def contador(* num): # * desempacotar para receber vários parametros ( Vou recever parametros, quantos? - Não sei.. se vera ai)
    print(num) # Neste caso criou uma tupla
    for i in num: # para cada Valor um num
        print(i, end=' ' )
    print('FIM')
    tam = len(num)
    print(f'Recebi os valor {num} e são ao todos {tam} numeros')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
#=================== EMPACOTAR PARAMETROS - LISTA ============================
#EX: Dobras os valores de uma lista com valores.
def dobra(lst): # A lista é uma variavel composta: Não precisa desempacotar.
    pos = 0 # começa na posição 0
    while pos < (len(lst)): # Enquado a posição for menor que o tamanho da lista:
        lst[pos]*=2 # A Lista na posição atual recebe o dobro.
        pos +=1


valores = (6, 3, 9, 1, 0, 2)
dobra(valores)
print(valores)
#==================================================================
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)