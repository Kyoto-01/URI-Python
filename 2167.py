qtd_testes = int(input())
rpms = input().split(maxsplit=qtd_testes)
rpms = [int(rpms[i]) for i in range(qtd_testes)]
primeira_queda = 0

for i in range(qtd_testes - 1):
    if rpms[i + 1] < rpms[i]:
        primeira_queda = i + 2
        break

print(primeira_queda)
