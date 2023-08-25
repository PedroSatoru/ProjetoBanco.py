# Pedro Henrique Satoru Lima Takahashi/ Gabriel Machado da Silva
# RA:22.123.019-6 / RA:22.123.005-5


# função para identificar o tempo, usada no extrato
from datetime import datetime

# mostrar todas as opções de funções no começo
print("1: Novo cliente")
print("2: Apaga cliente")
print("3: Listar clientes")
print("4: Débito")
print("5: Depósito")
print("6: Extrato")
print("7: Transferência entre contas")
print("8: Juncao de contas")
print("9: Sair")
print("10: Relistar as opções")

#listas nas quais serão armazenados os dados dos arquivos txt quando o programa iniciar
lista_clientes = []
lista_extrato = []

# função que ira ler as informações do aqruivo txt e dpois ira salvar essas informações temporiariamente na lista: "lista_clientes" acima
def ler_clientes():
    lista_clientes.clear()
    arquivo = open("lista.txt", "r")
    ler = arquivo.readlines()
    for x in ler:
        i = x.strip("\n").split(',')
        dicionario = {
            "nome": i[0],
            "cpf": i[1],
            "tipo_conta": i[2],
            "saldo": i[3],
            "senha": i[4]
        }
        lista_clientes.append(dicionario)
    arquivo.close()

#Função para salvar os clientes no arquivo "lista.txt" 
def salvar_clientes():
    arquivo = open("lista.txt", "w")
    for i in lista_clientes:
        arquivo.write("%s,%s,%s,%s,%s\n" % (
            i['nome'], i['cpf'], i['tipo_conta'], i['saldo'], i['senha']))
    arquivo.close()

#função para fazer o mesmo da "ler_clientes", mas para ler o extrato
def ler_extrato():
    lista_extrato.clear()
    arquivo = open("extrato.txt", "r")
    ler = arquivo.readlines()
    for x in ler:
        i = x.strip("\n").split(',')
        dicionario = {
            "nome": i[0],
            "cpf": i[1],
            "tipo_conta": i[2],
            "extrato": i[3],
        }
        lista_extrato.append(dicionario)
    arquivo.close()

#Função para salvar o extrato dos clientes em um arquivo txt
def salva_extrato():
    arquivo = open("extrato.txt", "w")
    for i in lista_extrato:
        arquivo.write("%s,%s,%s,%s\n" %
                      (i['nome'], i['cpf'], i['tipo_conta'], i['extrato']))
    arquivo.close()

# As 2 funções de leitura serão chamadas ao inicio de cada operação e ao iniciar o loop, e as duas funções de salvar serão chamadas ao 
# fim de cada operação.



# funcao novo cliente, atualmente está funcionando em formato de dicionario e verificando se o cliente já existe

def NovoCliente():
    #exemplo de como será usado a fução para ler os arquivos txt
    ler_clientes()
    ler_extrato()
    nome = input('Nome do cliente: ')
    cpf = input('CPF do cliente: ')
    tipo_conta = input('Tipo de conta (comum ou plus): ')
    saldo = float(input('Saldo inicial da conta: '))
    senha = input('Senha do cliente: ')
    cliente_encontrado = False
    for i in range(len(lista_clientes)):
        if lista_clientes[i]['cpf'] == cpf:
            cliente_encontrado = True
            print("Cliente já existe")
            break
    if not cliente_encontrado:
        lista_clientes.append({
            'nome': nome,
            'cpf': cpf,
            'tipo_conta': tipo_conta,
            'saldo': saldo,
            'senha': senha,
        })
        #exemplo de como será usado as funções de salvar os clientes em um arquivo txt
        salvar_clientes()
        #  Ao criarse um novo cliente, também é adicionado um dicionario com o extrato do mesmo cliente a uma lista de extratos ,
        #  extrato funcionando em formato de string
        lista_extrato.append({
            'nome': nome,
            'cpf': cpf,
            'tipo_conta': tipo_conta,
            'extrato': ""
        })
        salva_extrato()
        print("Cliente novo cadastrado com sucesso")


# funcao para apagar o cliente, já está funcionando em formato de dicionario
def ApagaCliente():
    ler_clientes()
    ler_extrato()
    cpf = input("Digite seu CPF: ")
    cliente_encontrado = False
    for i in range(len(lista_clientes)):
        if lista_clientes[i]['cpf'] == cpf:
            cliente_encontrado = True
            del lista_clientes[i]
            del lista_extrato[i]
            print("Cliente foi exlcluido")
            salvar_clientes()
            salva_extrato()
            break
    if not cliente_encontrado:
        print('Cliente não encontrado')


# funcao para listar os clientes esta funcional
def ListarCliente():
    print(lista_clientes)
    

# funcao debito está funcional, já esta considerando o tipo da conta do cliente, Salvando o extrato do cliente


def Debito():
    ler_clientes()
    ler_extrato()
    data = datetime.now()
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    valor = float(input("Digite o valor a ser debitado: "))
    for i in range(len(lista_clientes)):
        if lista_clientes[i]['cpf'] == cpf and lista_clientes[i]['senha'] == senha:
            if lista_clientes[i]['tipo_conta'] == "plus":
                (lista_clientes[i]['saldo']) = float(
                    lista_clientes[i]['saldo'])-valor*1.03
                # caso o saldo do cliente apos a operação for menor que o disponivel pelo tipo de conta, ele recebera o dinheiro
                #  de volta e a operação sera cancelada
                if lista_clientes[i]['saldo'] < -5000:
                    lista_clientes[i]['saldo'] = float(
                        lista_clientes[i]['saldo'])+valor*1.03
                    print("Saldo insuficiente")
                    return
                print("valor debitado com sucesso")
                salvar_clientes()
                # caso a operação der certo, o dia, mes, ano e horario que a operação foi feita serão salvos no dicionario
                #  do extrato
                for a in range(len(lista_extrato)):
                    if lista_extrato[a]['cpf'] == cpf:
                        lista_extrato[a]['extrato'] += ("%.19s - %s  Tarifa: 0.03   Saldo: %s!" % (
                            data, valor, lista_clientes[i]['saldo']))
                        salva_extrato()
                return
            if lista_clientes[i]['tipo_conta'] == "comum":
                lista_clientes[i]['saldo'] = float(
                    lista_clientes[i]['saldo'])-valor*1.05
                if lista_clientes[i]['saldo'] < -1000:
                    lista_clientes[i]['saldo'] = float(
                        lista_clientes[i]['saldo'])+valor*1.05
                    print("Saldo insuficiente")
                    return
                print("Valor debitado com sucesso")
                salvar_clientes()
                for a in range(len(lista_extrato)):
                    if lista_extrato[a]['cpf'] == cpf:
                        lista_extrato[a]['extrato'] += ("%.19s - %s  Tarifa: 0.05   Saldo: %s!" % (
                            data, valor, lista_clientes[i]['saldo']))
                        salva_extrato()

                return
    print("Senha ou CPF incorretos")


# funcao deposito totalmente funcional
def Deposito():
    ler_clientes()
    data = datetime.now()
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    valor = float(input("Digite o valor a ser depositado: "))
    for i in range(len(lista_clientes)):
        if lista_clientes[i]['cpf'] == cpf and lista_clientes[i]['senha'] == senha:
            lista_clientes[i]['saldo'] = float(
                lista_clientes[i]['saldo'])+valor
            print("Valor depositado com sucesso")
            salvar_clientes()
            for a in range(len(lista_extrato)):
                if lista_extrato[a]['cpf'] == cpf:
                    lista_extrato[a]['extrato'] += ("%.19s + %s  Tarifa: 0.00   Saldo: %s!" % (data, valor, lista_clientes[i]['saldo']))
                    salva_extrato()
                    
            return
    
    print("Senha ou CPF incorretos")


# funcao extrato totalmente funcional, funcionando em formato de dicionario,
# imprimindo um abaixo do outro de forma correta
def Extrato():
    ler_extrato()
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")

    for i in range(len(lista_clientes)):
        if lista_clientes[i]['cpf'] == cpf and lista_clientes[i]['senha'] == senha:
            for x in range(len(lista_extrato)):
                if lista_extrato[x]['cpf'] == cpf:
                    print("Nome: "+lista_extrato[x]['nome'])
                    print("Tipo da conta: " + lista_extrato[x]['tipo_conta'])
                    a = lista_extrato[x]['extrato'].split("!")
                    for i in a:
                        print(i)          
                        salva_extrato()
                        return
    print("Senha ou CPF incorretos")

# funcao para transefrencia entre contas totalmente funcional, e caso erre a senha ou o cpf cancela a operação


def TansferenciaEntreContas():
    ler_extrato()
    ler_clientes()
    data = datetime.now()
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    cpf2 = input("Digite o cpf do destinatario: ")
    valor = float(input("Digite o valor a transefrido: "))
    for i in range(len(lista_clientes)):
        if lista_clientes[i]['cpf'] == cpf and lista_clientes[i]['senha'] == senha:
            for x in range(len(lista_clientes)):
                if lista_clientes[x]['cpf'] == cpf2:
                    lista_clientes[x]['saldo'] = float(
                        lista_clientes[x]['saldo'])+valor
                    lista_clientes[i]['saldo'] = float(
                        lista_clientes[i]['saldo'])-valor
                    if lista_clientes[i]['tipo_conta'] == "plus":
                        # verificando se o clinte que está transferindo tem o saldo necessario para a operação
                        if lista_clientes[i]['saldo'] < -5000:
                            lista_clientes[i]['saldo'] = float(
                                lista_clientes[i]['saldo'])+valor
                            print("Saldo insuficiente")
                            return
                    if lista_clientes[i]['tipo_conta'] == "comum":
                        if lista_clientes[i]['saldo'] < -1000:
                            lista_clientes[i]['saldo'] = float(
                                lista_clientes[i]['saldo'])+valor
                            print("Saldo insuficiente")
                            return
                    # salvando o extrato para cada um dos clientes
                    for a in range(len(lista_extrato)):
                        if lista_extrato[a]['cpf'] == cpf:
                            lista_extrato[a]['extrato'] += ("%.19s - %s  Tarifa: 0.00   Saldo: %s!" % (
                                data, valor, lista_clientes[i]['saldo']))
                            salva_extrato()
                    for b in range(len(lista_extrato)):
                        if lista_extrato[b]['cpf'] == cpf2:
                            lista_extrato[b]['extrato'] += ("%.19s + %s  Tarifa: 0.00   Saldo: %s!" % (
                                data, valor, lista_clientes[x]['saldo']))
                            salva_extrato()
                    print("Valor transefrido com sucesso")
                    salvar_clientes()
                    return
    print("cpf ou senha errados")


# Função para juntar a conta de dois clientes em uma unica conta (Os usuarios escolhem qual conta será a principal)
def juncaoConta():
    ler_extrato()
    ler_clientes()
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    cpf2 = input("Digite o cpf do parceiro(a): ")
    senha2 = input("Digite a senha do parceiro(a): ")
    principal = input("Qual sera a conta principal(1 ou 2): ")
    senha_nova = input("Digite a senha nova: ")
    for i in range(len(lista_clientes)):
        if lista_clientes[i]['cpf'] == cpf and lista_clientes[i]['senha'] == senha:
            for x in range(len(lista_clientes)):
                if lista_clientes[x]['cpf'] == cpf2 and lista_clientes[x]['senha'] == senha2:
                    # caso a conta principal escolhida seja a "1", o saldo da conta 2 sera adicionado ao saldo da conta 1,
                    # será criado uma nova senha e a conta 2 será apagada
                    if principal == "1":
                        lista_clientes[i]['saldo'] = float(lista_clientes[i]['saldo']) + float(lista_clientes[x]['saldo'])
                        lista_clientes[i]['senha'] = senha_nova
                        del lista_clientes[x]
                        del lista_extrato[x]
                        print("O seu parceiro(a) juntou a conta com você com sucesso")
                        salvar_clientes()
                        salva_extrato()
                        return
                    # caso a conta principal escolhida seja a "2", o saldo da conta 1 sera adicionado ao saldo da conta 2,
                    # será criado uma nova senha e a conta 1 será apagada
                    if principal == "2":
                        lista_clientes[x]['saldo'] = float(lista_clientes[x]['saldo']) +  float(lista_clientes[i]['saldo'])
                        lista_clientes[x]['senha'] = senha_nova
                        del lista_clientes[i]
                        del lista_extrato[i]
                        print("voce juntou a sua conta com seu parceiro(a) com sucesso")
                        salvar_clientes()
                        salva_extrato()
                        return
    print("cpf ou senha errado")


def repetir_funcoes():
    print("1: Novo cliente")
    print("2: Apaga cliente")
    print("3: Listar clientes")
    print("4: Débito")
    print("5: Depósito")
    print("6: Extrato")
    print("7: Transferência entre contas")
    print("8: Juncao de contas")
    print("9: Sair")
    print("10: Relistar as opções")


# Laco de repeticao
while True:
    #as duas funções de ler tambm são chhamadas ao inicio do loop, para assim atualizar as listas que armazenam as informações do txt
    ler_clientes()
    ler_extrato()
    op = (input("Digite a opção: "))
    if op == "9":
        print("Voce saiu, volte sempre")
        break
    elif op == "1":
        NovoCliente()
    elif op == "2":
        ApagaCliente()
    elif op == "3":
        ListarCliente()
    elif op == "4":
        Debito()
    elif op == "5":
        Deposito()
    elif op == "6":
        Extrato()
    elif op == "7":
        TansferenciaEntreContas()
    elif op == "8":
        juncaoConta()
    elif op == "10":
        repetir_funcoes()
    else:
        print("Opção invalida")
