a, b = input().split()
a, b = int(a), int(b)
duracao = 0

if (a < b):
    duracao = b - a
else:
    duracao = 24 - (a - b)

print('O JOGO DUROU', duracao, 'HORA(S)')
