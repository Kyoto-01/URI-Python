col = int(input())
op = input()

matriz = []
for i in range(12):
    matriz.append([])
    for j in range(12):
        matriz[i].append(float(input()))

soma_col = 0
for lin in matriz:
    soma_col += lin[col]

media = soma_col / len(matriz[0])
saida = (soma_col if op == 'S'
         else media if op == 'M'
         else 0)

print(f'{saida:.1f}')
