def validacao():
    nota = float(input())

    while (nota < 0) or (nota > 10):
        print('nota invalida')
        nota = float(input())

    return nota


n1 = validacao()
n2 = validacao()
media = (n1 + n2) / 2

print('media = {:.2f}'.format(media))
