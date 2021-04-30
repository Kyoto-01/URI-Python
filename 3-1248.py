n = int(input())

for i in range(n):
    dieta = input()
    cafe = input()
    almoco = input()
    refeicoes = cafe + almoco

    cheater = False
    for j in refeicoes:
        if refeicoes.count(j) > dieta.count(j):
            cheater = True
            break

    if not cheater:
        jantar = ''
        for k in dieta:
            if k not in refeicoes:
                jantar += k
        print(''.join(sorted(jantar)))
    else:
        print("CHEATER")
