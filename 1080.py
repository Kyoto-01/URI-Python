maior = 0
posicao_do_maior = 0

for i in range(100):
    val = int(input())

    if val > maior:
        maior = val
        posicao_do_maior = i + 1

print(f'{maior}\n{posicao_do_maior}')
