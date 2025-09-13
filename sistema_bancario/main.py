# Desafio DIO
def main ():
    opcao = -1
    while opcao != 4:
        print('##### SISTEMA BANCÁRIO DIO #####')
        print('[1] - SAQUE')
        print('[2] - DEPÓSITO')
        print('[3] - EXTRATO')
        print('[4] - SAIR')
        try:
            opcao = int(input('Digite o número da operação: '))
            if opcao == 1:
                pass    # sacar
            elif opcao == 2:
                pass    # depositar
            elif opcao == 3:
                pass    # visualizar extrato
            elif opcao == 4:
                print('Encerrando aplicação...')
            else:
                print('Opção inválida!')
        except ValueError:
            print('ERRO: INFORME UM VALOR INTEIRO.')

main()