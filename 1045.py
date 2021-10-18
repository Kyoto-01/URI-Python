# 17 min

a, b, c = sorted(map(float, input().split(maxsplit=3)), reverse=True)

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    if a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    if (a == b and a != c != b) or (a == c and a != b != c) or (b == c and b != a != c):
        print('TRIANGULO ISOSCELES')
