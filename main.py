# Lista de nomes
nomes = []

# inicio do loop
while True:
    # menu
    print('1 - Inserir novo nome.')
    print('2 - Exibir Lista de Nomes.')
    print('3 - Exibir em Ordem Alfabética.')
    print('4 - Sair do Programa.')

    # opção do usuário
    opcao = input('Opcao do Uusário: ')

    # verifica a opção escolhida
    match opcao:
        case '1':
            novo_nome = input('Insira o novo nome: ').capitalize()
            nomes.append(novo_nome)
            print(f'{novo_nome} inserido com sucesso.')
            continue
        case '2':
            print('\nLista de Nomes:\n')
            for nome in nomes:
                print(nome)
                continue
        case '3':
            nomes.sort()
            for nome in nomes:
                print(nome)
            print('\nLista ordenada com sucesso.')
            continue
        case '4':
            print('Programa encerrado')
            break
        case _:
            print('Opção inválida.')
    
          

    

