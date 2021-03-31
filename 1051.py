salario = float(input())

if (salario > 2000):
    imposto = 0
    
    if (salario >= 2000.01 and salario <= 3000):
        salario -= 2000
        imposto = (salario * .08)
    elif (salario >= 3000.01 and salario <= 4500):
        salario -= 2000 + 1000
        imposto = (1000 * 0.08) + (salario * 0.18)
    else:
        salario -= 2000 + 1000 + 1500
        imposto = (1000 * 0.08) + (1500 * 0.18) + (salario * 0.28)
        
    print(f'R$ {imposto:.2f}')
else:
    print('Isento')
