print ('1- Soma')
print ('2- Subtração')
print ('3- Multiplicação')
print ('4- Divisão')

while True:
    opção = int (input ('Digite uma das opções: '))
    if opção > 0 and  opção < 5:
        return
    elif opção == 0:
        break
    else:
        print ('Opção invalida')
