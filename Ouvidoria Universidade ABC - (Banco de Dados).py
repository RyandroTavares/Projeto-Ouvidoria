import OperacoesSQL
abrir = OperacoesSQL.abrirBancoDados('localhost','root','amarajairla','ouvidoria') #Adentrar no banco de dados

listaTipos = ['Reclamação', 'Sugestão', 'Elogio'] #Lista de tipos da manifestações
opcao = quantidade = 0

while opcao != 7: #Começo do Menu
    print()
    print('===== Aplicativo Ouvidoria Universidade ABC =====')
    print('1) Listar Todas as Manifestações')
    print('2) Listar Todas as Reclamações')
    print('3) Listar Todas as Sugestões')
    print('4) Listar Todos os Elogios')
    print('5) Criar uma Nova Manifestação')
    print('6) Procurar Manifestação por Protocolo(ID)')
    print('7) Sair')
    print()
    opcao = int(input('Digite a opção do menu: '))
    print() #Fim do Menu

    if opcao < 1 or opcao > 7: #Começo para confirmar se o número informado existe no menu
        print('Não existe essa opção no menu, tente novamente!') #Fim do confirmar

    elif opcao == 1: #Começo da lista de manifestações
        sql = "SELECT * FROM manifestacoes"
        resultado = OperacoesSQL.listarBancoDados(abrir,sql)
        print('Lista de todas manifestações!')
        for i in resultado:
            elemento = str('Protocolo: {}, Requisitante: {}, Tipo da Manifestação: {}, Descrição: {}'.format(i[0], i[1], i[2], i[3]))
            print(elemento) #Fim 'Protocolo: {i[0]}, Requisitante: {i[1]}, Tipo da Manifestação: {i[2]}, Descrição: {i[3]}'da lista de manifestações

    elif opcao == 2: #Começo da lista de reclamações
        sql = "SELECT * FROM manifestacoes where tipo = 'Reclamação'"
        resultado = OperacoesSQL.listarBancoDados(abrir,sql)
        print('Lista de todas reclamações!')
        for i in resultado:
            elemento = str('Protocolo: {}, Requisitante: {}, Descrição: {}'.format(i[0], i[1], i[3]))
            print(elemento) #Fim da lista de reclamações

    elif opcao == 3: #Começo da lista de sugestões
        sql = "SELECT * FROM manifestacoes where tipo = 'Sugestão'"
        resultado = OperacoesSQL.listarBancoDados(abrir,sql)
        print('Lista de todas sugestões!')
        for i in resultado:
            elemento = str('Protocolo: {}, Requisitante: {}, Descrição: {}'.format(i[0], i[1], i[3]))
            print(elemento) #Fim da lista de sugestões

    elif opcao == 4: #Começo da lista de elogios
        sql = "SELECT * FROM manifestacoes where tipo = 'Elogio'"
        resultado = OperacoesSQL.listarBancoDados(abrir,sql)
        print('Lista de todos elogios!')
        for i in resultado:
            elemento = str('Protocolo: {}, Requisitante: {}, Descrição: {}'.format(i[0], i[1], i[3]))
            print(elemento) #Fim da lista de elogios

    elif opcao == 5: #Começo do criador de manifestações
        tipo = 0
        requisitante = input('digite o nome do requisitante: ')
        while tipo < 1 or tipo > 3: #Repetir caso o usuario digite o número abaixo errado
            tipo = int(input('Digite o Tipo da manifestação: [1) Reclamação, 2) Sugestão e 3) Elogio]: ')) #Saber o tipo da manifestação
            if tipo < 1 or tipo > 3: #Chegar se o número informado é válido
                print('Tipo de manifestação inválido tente novamente!')
        descricao = input('Digite a descrição: ')
        sql = "INSERT INTO manifestacoes (requisitante, tipo, descricao) VALUES (%s, %s, %s)"
        dados = (requisitante, listaTipos[tipo-1], descricao)
        OperacoesSQL.insertNoBancoDados(abrir,sql,dados)
        #Fim do criador de manifestações
    
    elif opcao == 6:
        sql = "SELECT * FROM manifestacoes"
        resultado = OperacoesSQL.listarBancoDados(abrir,sql)
        quantidade = len(resultado)
        print('Protocolos Disponíveis: [{}]'.format(quantidade)) #Mostra quanto protocolos existe
        pesquisa = int(input('Digite o número do seu protocolo: ')) #Pesquisa para escolher o protocolo
        if pesquisa < 1 or pesquisa > quantidade:
            print('Protocolo informado não existe ou é inválido!')
        else:
            for i in resultado:
                if i[0] == pesquisa:
                    elemento = str('Protocolo: {}\nRequisitante: {}\nTipo da Manifestação: {}\nDescrição: {}'.format(i[0], i[1], i[2], i[3]))
                    print()
                    print(elemento)

print('Saindo...')
OperacoesSQL.encerrarBancoDados(abrir)