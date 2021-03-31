x, y = input().split()
x, y = int(x), int(y)

while (x != y):
        if (x < y):
            print('Crescente')
        else:
            print('Decrescente')

        x, y = input().split()
        x, y = int(x), int(y)