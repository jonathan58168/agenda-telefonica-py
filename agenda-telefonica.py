agenda = {}

while True:
    print('------- Agenda telefonica -------')
    print('1 - Adicionar contato')
    print('2 - Editar contato')
    print('3 - Remover contato')
    print('4 - Buscar contato')
    print('5 - Listar todos')
    print('6 - Sair')
    print('----------------------------------')
    opc = int(input('\033[32mSelecione uma opção: \033[m'))
    if opc == 1:
        nome = input('\033[33mDigite o nome do contato: \033[m')
        telefone = input('Digite o telefone do contato: ')
        agenda[nome] = telefone
        print('Contato adicionado com sucesso!')
    elif opc == 2:
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            agenda[nome] = input('Digite o novo telefone: ')
            print('Telefone alterado com sucesso!')
        else:
            print('Contato não encontrado!')
    elif opc == 3:
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            del agenda[nome]
            print('Contato removido com sucesso!')
        else:
            print('Contato não encontrado!')
    elif opc == 4:
        nome = input('Digite o nome do contato: ')
        if nome in agenda:
            print(f'Telefone do {nome}: {agenda[nome]}')
        else:
            print('Contato não encontrado!')
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