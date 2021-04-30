qtd_pecas = int(input())
tamanho_tabuleiro = int(input())
tabuleiro = [[0] * tamanho_tabuleiro for i in range(tamanho_tabuleiro)]

qtd_descarte = 0
for i in range(qtd_pecas):
    lin, col = input().split(maxsplit=2)
    lin, col = int(lin), int(col)

    if tabuleiro[lin][col] == 1:
        qtd_descarte += 1
    else:
        tabuleiro[lin][col] = 1

print(qtd_descarte == 0)
print(qtd_descarte)
