pos_qtd = pos_sum = 0

for i in range(6):
    num = float(input())

    if num > 0:
        pos_qtd += 1
        pos_sum += num

media = pos_sum / pos_qtd

print(pos_qtd, 'valores positivos')
print(f'{media:.1f}')
