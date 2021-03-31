idade = int(input())
soma_idades = 0
qtd_idades = 0

while (idade >= 0):
    soma_idades += idade
    qtd_idades += 1
    idade = int(input())

media = soma_idades / qtd_idades

print(f'{media:.2f}')
