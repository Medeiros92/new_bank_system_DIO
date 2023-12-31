    #MENU INICIAL
def menu_ini(): 
     return """
    OPERAÇÕES:

[1] Cadastrar
[2] Tenho Conta
[3] Listar Clientes
[4] Sair

=> """

    #MENU CLIENTE
def menu_cliente():
    return """
    OPERAÇÕES:

[1] Abrir uma nova conta
[2] Operações
[3] Sair

=> """
    #MENU OPERAÇÕES
def menu_op():
    return """
    OPERAÇÕES:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

    #DECLARAÇÃO DE VARIÁVEIS
saldo = 0
lim_saque = 3
val_max_saque = 500
extrato = ""
num_saque = 0
num_conta = 0
clientes = []
cliente = {}
cpf_dup = ""
conta_bancaria = []
conta = []
borda = "*" * 133


    #Função LISTA CPF
def lista_cpf(cpf):
     
        #Pecorre toda a Lista Clientes
     for i in range(0, len(clientes)):

            #Verifica se já existe o cpf cadastrado no Dicionário
            if clientes[i]['cpf'] == cpf:
                return "Este CPF já está cadastrado."

    #FUNÇÃO LISTA NOME POR CPF
def lista_n_cpf(cpf):
    for i in range(0, len(clientes)):
        if clientes[i]['cpf'] == cpf:
            return clientes[i]['nome']
        
        
    #FUNÇÃO CADASTRO CLIENTE
def cad_cliente(nome_c, data_n, cpf_c, logradouro, nro, bairro, cidade, sig_estado):
    cliente = {"nome": nome_c, "data_nascimento":data_n, "cpf": cpf_c, "endereco": f"{logradouro}, {nro} - {bairro} - {cidade}/{sig_estado}"}
    global clientes
    clientes.append(cliente)
    return 

    #FUNÇÃO CADASTRO CONTA BANCÁRIA
def cad_conta_bancaria(nome):
    num_agencia = "0001"
    global num_conta
    num_conta += 1
    conta = [num_agencia, num_conta, nome]
    global conta_bancaria
    conta_bancaria.append(conta)

    return

    #FUNÇÃO DEPOSITAR
def depositar(valord, sal, ext):
    if valord > 0:
        sal += valord
        global saldo
        saldo = sal
        ext += f"Depósito: R$ {valord:.2f}\n"
        global extrato
        extrato = ext
    else:
        return "***Operação falhou! O valor informado é inválido.***"

    #FUNÇÃO SACAR
def sacar(* valors, sal, ext, ):    

    if valors > 0:
        
        if sal > valors:
            
            if valors <= val_max_saque:
                
                sal -= valors
                global saldo 
                saldo = sal
                ext += f"Saque: R$ {valors:.2f}\n"
                global extrato
                extrato = ext

            else:
                return f"***Operação falhou! O limite de saque é de R$ {val_max_saque:.2f}***"
        else:
            return "***Operação falhou! Você não tem saldo suficiente.***"
    else:
            return "***Operação falhou! O valor informado é inválido.***"
                        
    #FUNÇÃO EXTRATO
def f_extrato(ext):
            global extrato
            extrato = ext
            if not extrato:
                return"\n***Nenhum movimento foi registrado.***"     
            else:
                return f"""
========== Extrato ==========

{extrato}

Saldo Atual: R$ {saldo:.2f}
============================="""

    # MENU INICIAL
while True:
     
    opcao = input(menu_ini())

    # OPÇÃO CADASTRAR
    if opcao == "1":
        print("Por favor, informe seus Dados.\n")
        nome_c = input("Nome: ") 
        data_n = input("Data de nascimento: ")
        cpf_c = input("CPF: ")

        #Chama função lista_cpf passando a variavel cpf_c como parametro
        cpf_dup = lista_cpf(cpf_c)

                #Se o valor da variável for diferente da String, continua o cadastro
        if cpf_dup != "Este CPF já está cadastrado.":
            logradouro = input("Logradouro: ")
            nro = input("Número: ")
            bairro = input("Bairro: ")
            cidade = input("Cidade: ")
            sig_estado = input("Sigla do Estado: ")
            cad_conta_bancaria(nome_c)
            cad_cliente(nome_c, data_n, cpf_c, logradouro, nro, bairro, cidade, sig_estado)
            
            #Se não, ele mostra o texto, Limpa o valor da variavel, imterrompe o cadastro e volta para o menu inicial.
        else:
             print(f"\n{cpf_dup}\nCadastro Cancelado.\n")
             cpf_dup = ""
             continue

    # OPÇÃO TENHO CONTA
    elif opcao == "2":
        cpf_t = input("Digite seu CPF: ")
        cpf_e = lista_cpf(cpf_t)
        print()

            #Se o cpf estiver cadastrado a lista ele quebrará a repetição do menu inicial e entrará no menu cliente.
        if cpf_e == "Este CPF já está cadastrado.":

                #MENU CLIENTE
            while True:
                opcao = input(menu_cliente())

                    #OPÇÃO ABRIR NOVA CONTA
                if opcao == "1":

                        #Chama a função lista nome por cpf 
                        #Passando o parametro cpf digitado na opção Tenho Conta do Menu inicial
                        #Variavel nome_e recebe o resultado
                    nome_e = lista_n_cpf(cpf_t)

                        #Chama a função cad_conta_bancaria passando a variavel nome_e como parametro.
                    cad_conta_bancaria(nome_e)
                    

                    #OPÇÃO OPERAÇÕES
                elif opcao == "2":

                    #MENU OPERAÇÕES
                    while True:
                        
                        opcao = input(menu_op())
                        
                        if opcao == "1":
                            valor = float(input("Informe o valor a ser depositado: "))
                            print(depositar(valor, saldo, extrato))
                                
                        elif opcao == "2":
                            
                            if lim_saque > num_saque:
                                lim_saque -=1
                                valor = float(input("Informe o valor do saque: "))
                                
                                print(sacar(valor=valor, sal=saldo, ext=extrato))
                                    
                            else:
                                print("***Operação falhou! Você atingiu o número maximo de saques diários.***")
                                
                        elif opcao =="3":
                            print(f_extrato(ext=extrato))  
                                
                        elif opcao == "4":
                            break
                            
                        else:
                            print("***Opção Inválida.***")
                    break

                    #OPÇÃO SAIR
                elif opcao == "3":
                    break
                
                else:
                    print("***Opção Inválida.***")
                    break
        
        else:
             print()
             print("Este CPF não está registrado em nosso sistema.")
             print()

    # OPÇÃO LISTAR CLIENTES
    elif opcao == "3":
        for i in range(0, len(clientes)):
            nome = clientes[i]['nome']
            d_nascimento = clientes[i]['data_nascimento']
            cpf = clientes[i]['cpf']
            endereco = clientes[i]['endereco']
            print(f"   CLIENTES CADASTRADOS\n{borda}")
            print(f"Cliente {i}\n")
            print(f"Nome: {nome}\nDATA DE NASCIMENTO: {d_nascimento}\nCPF: {cpf}\nENDEREÇO: {endereco}")
            print(f"{borda}")
        for i in range(0, len(conta_bancaria)):
            agencia = conta_bancaria[i][0]
            conta = conta_bancaria[i][1]
            nome = conta_bancaria[i][2]
            print(f"   CONTAS BANCÁRIAS CADASTRADAS\n{borda}")
            print(f"Conta {i}\n")
            print(f"AGÊNCIA: {agencia}\nCONTA: {conta}\nCLIENTE: {nome}")
            print(f"{borda}")
         
              
   # OPÇÃO SAIR
    elif opcao == "4":
        break 
      
    else:
        print("***Opção Inválida.***")




         



