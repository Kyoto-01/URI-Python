n = int(input())
total = 0
coelhos = coelhos_percent = 0
ratos = ratos_percent = 0
sapos = sapos_percent = 0

for i in range(n):
    quantia, tipo = input().split()
    quantia, tipo = int(quantia), str(tipo).upper()
    total += quantia

    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

coelhos_percent = (coelhos / total) * 100
ratos_percent = (ratos / total) * 100
sapos_percent = (sapos / total) * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {coelhos_percent:.2f} %')
print(f'Percentual de ratos: {ratos_percent:.2f} %')
print(f'Percentual de sapos: {sapos_percent:.2f} %')
