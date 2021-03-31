cod1, qtd1, val1 = input().split()
cod2, qtd2, val2 = input().split()

cod1, qtd1, val1 = int(cod1), int(qtd1), float(val1)
cod2, qtd2, val2 = int(cod2), int(qtd2), float(val2)

preco_total = (val1 * qtd1) + (val2 * qtd2)

print('VALOR A PAGAR: R$ {:.2f}'.format(preco_total))
