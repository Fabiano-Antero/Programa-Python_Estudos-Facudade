def menu():
    
    print('1 - Soma')
    print('2 - Sulbitrasão ')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('0 - Sair')

    while True:

        opcao = int(input('Digite uma opçao: '))
        if opcao >= 0 and  opcao <= 4:
            return opcao
        print('Opção invalida caralho!')
