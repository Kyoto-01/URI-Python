pares = positivos = 0

for i in range(5):
    val = int(input())

    if val % 2 == 0:
        pares += 1
    if val > 0:
        positivos += 1

print(pares, 'valor(es) par(es)')
print(5 - pares, 'valor(es) impar(es)')
print(positivos, 'valor(es) positivo(s)')
print(4 - positivos, 'valor(es) negativo(s)') # 4 por causa do 0, que é neutro
