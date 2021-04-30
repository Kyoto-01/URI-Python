op = input()

tamanho_matriz = 12
matriz = []
for i in range(tamanho_matriz):
    matriz.append([])
    for j in range(tamanho_matriz):
        matriz[i].append(float(input()))

soma_diagonal = 0
qtd_indexes_diagonal = 0
for i in range(tamanho_matriz):
    for j in range(1 + i, tamanho_matriz):
        soma_diagonal += matriz[i][j]
        qtd_indexes_diagonal += 1

media = soma_diagonal / qtd_indexes_diagonal
saida = (soma_diagonal if op == 'S'
         else media if op == 'M'
         else 0)

print(f'{saida:.1f}')
