cod = 0
alcool = gasolina = diesel = 0

while (cod != 4):
    cod = int(input())

    if (cod == 1):
        alcool += 1
    elif (cod == 2):
        gasolina += 1
    elif (cod == 3):
        diesel += 1

print('MUITO OBRIGADO')
print('Alcool:', alcool)
print('Gasolina:', gasolina)
print('Diesel:', diesel)
