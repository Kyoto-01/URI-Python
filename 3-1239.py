# converte símbolos para HTML

while True:
    try:
        texto = input()
        texto_html = ''

        italico_aberto = False
        negrito_aberto = False

        for i in texto:
            char = i
            if i == '_':
                char = '</i>' if italico_aberto else '<i>'
                italico_aberto = not italico_aberto
            elif i == '*':
                char = '</b>' if negrito_aberto else '<b>'
                negrito_aberto = not negrito_aberto

            texto_html += char

        print(texto_html)
    except EOFError:
        break
