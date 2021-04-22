def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um numero: '))
print(f'O Fatorial de {n} é igual {fatorial(n)}')

#Outro exemplo

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resulado {f1} {f2} {f3}')