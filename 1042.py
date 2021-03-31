a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

#sort em ordem crescente
if ((a > b) and (a > c)):
    #a p. maior
    if (b > c):
        #b s. maior
        print(f'{c}\n{b}\n{a}')
    else:
        #c s. maior
        print(f'{b}\n{c}\n{a}')
elif ((b > a) and (b > c)):
    #b p. maior
    if (c > a):
        #c s. maior
        print(f'{a}\n{c}\n{b}')
    else:
        #a s. maior
        print(f'{c}\n{a}\n{b}')
else:
    #c p. maior
    if (a > b):
        #a s. maior
        print(f'{b}\n{a}\n{c}')
    else:
        #b s. maior
        print(f'{a}\n{b}\n{c}')
        
print(f'\n{a}\n{b}\n{c}')
