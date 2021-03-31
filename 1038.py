cod, qtd = input().split()
cod, qtd = int(cod), int(qtd)

cods = [4.0, 4.5, 5.0, 2.0, 1.5]
conta = cods[cod - 1] * qtd

print('Total: R$ {:.2f}'.format(conta))
