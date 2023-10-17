agenda = {}

while True:
    print('------- Agenda telefonica -------')
    print('1 - \033[34mAdicionar contato\033[m')
    print('2 - \033[34mEditar contato\033[m')
    print('3 - \033[34mRemover contato\033[m')
    print('4 - \033[34mBuscar contato\033[m')
    print('5 - \033[34mListar todos\033[m')
    print('6 - \033[34mSair\033[m')
    print('----------------------------------')
    opc = int(input('\033[32mSelecione uma opção: \033[m'))
    if opc == 1:
        nome = input('\033[33mDigite o nome do contato: \033[m')
        telefone = input('\033[33mDigite o telefone do contato: \033[m')
        agenda[nome] = telefone
        print('\033[35mContato adicionado com sucesso!\033[m')
    elif opc == 2:
        nome = input('\033[33mDigite o nome do contato: \033[m')
        if nome in agenda:
            agenda[nome] = input('\033[33mDigite o novo telefone: \033[m')
            print('\033[35mTelefone alterado com sucesso!\033[m')
        else:
            print('\033[31mContato não encontrado!\033[m')
    elif opc == 3:
        nome = input('\033[33mDigite o nome do contato: \033[m')
        if nome in agenda:
            del agenda[nome]
            print('\033[31mContato removido com sucesso!\033[m')
        else:
            print('\033[31mContato não encontrado!\033[m')
    elif opc == 4:
        nome = input('\033[33mDigite o nome do contato: \033[m')
        if nome in agenda:
            print(f'Telefone do {nome}: {agenda[nome]}')
        else:
            print('\033[31mContato não encontrado!\033[m')
    elif opc == 5:
        print('------TODOS OS CONTATOS------')
        for nome in agenda:
            print(f'Nome: {nome} - Telefone: {agenda[nome]}')
    elif opc == 6:
        print('Programa encerrado, até logo!')
        inicio = input('Deseja iniciar o sistema S/N?')
        if inicio == 's':
            continue
        elif inicio == 'n':
            break
    else:
        print('Opção inválida')
