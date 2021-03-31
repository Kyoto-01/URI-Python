a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

delta = (b ** 2) - (4 * a * c)

if (delta > 0 and a != 0):
    delta **= .5
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)

    print('R1 = {0:.5f}\nR2 = {1:.5f}'.format(x1, x2))
else:
    print('Impossivel calcular')  
