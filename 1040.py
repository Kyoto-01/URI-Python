nota1, nota2, nota3, nota4 = input().split()
nota1, nota2, nota3, nota4 = float(nota1), float(nota2), float(nota3), float(nota4)

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + nota4) / 10
print(f'Media: {media:.1f}')

if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')

    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')

    media = (media + nota_exame) / 2

    if media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(f'Media final: {media:.1f}')
