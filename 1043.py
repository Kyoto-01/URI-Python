a, b, c = map(float, input().split(maxsplit=3))

if abs(a - b) < c < (a + b):
    print(f'Perimetro = {(a + b + c):.1f}')
else:
    print(f'Area = {(((a + b) * c) / 2):.1f}')
