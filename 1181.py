linha = int(input())
operacao = input()
resultado = 0
matriz = []

for i in range(12):
    matriz.append([])
    for j in range(12):
        matriz[i].append(float(input()))

resultado = sum(matriz[linha])
if operacao == 'M':
    resultado = resultado / len(matriz[linha])

print(resultado)
