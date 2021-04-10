n = int(input())
x = input().split(maxsplit=n)
x = [int(x[i]) for i in range(n)]

menor = min(x)
print(f'Menor valor: {menor}')
print(f'Posicao: {x.index(menor)}')
