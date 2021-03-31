qtd_grenais = 0
vitorias_inter = 0
vitorias_gremio = 0
empates = 0

repeticao = '1'
while (repeticao == '1'):
    inter, gremio = input().split()
    inter, gremio = int(inter), int(gremio)
    qtd_grenais += 1

    if (inter > gremio):
        vitorias_inter += 1
    elif (gremio > inter):
        vitorias_gremio += 1
    else:
        empates += 1

    print('Novo grenal (1-sim 2-nao)')
    repeticao = input()

print(f'{qtd_grenais} grenais')
print(f'Inter:{vitorias_inter}')
print(f'Gremio:{vitorias_gremio}')
print(f'Empates:{empates}')

if (vitorias_inter > vitorias_gremio):
    print('Inter venceu mais')
elif (vitorias_gremio > vitorias_inter):
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')


