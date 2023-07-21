    #Menu Inicial
menu_ini = """
    OPERAÇÕES:

[1] Cadastrar
[2] Tenho Conta
[3] Sair

=> """
    #Menu Cliente
menu_cliente = """
    OPERAÇÕES:

[1] Abrir uma nova conta
[2] Operações
[3] Sair

=> """
    #Menu Operações
menu_op = """
    OPERAÇÕES:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

    #Declaração de Variáveis
saldo = 0
lim_saque = 3
val_max_saque = 500
extrato = ""
num_saque = 0
clientes = []
cliente = {}
cpf_dup = ""

    #Função Cadastro Cliente
def cad_cliente(nome_c, data_n, cpf_c, logradouro, nro, bairro, cidade, sig_estado):
    cliente = {"nome": nome_c, "data_nascimento":data_n, "cpf": cpf_c, "endereco": f"{logradouro}, {nro} - {bairro} - {cidade}/{sig_estado}"}
    global clientes
    clientes.append(cliente)
    return 

    #Função Cadastro Conta Bancaria
def cad_conta_bancaria():
    return

    #Função Depositar
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

    #Função Sacar
def sacar(valors, sal, ext):    

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
                        
    #Função Extrado
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
     
    opcao = input(menu_ini)

    # OPÇÃO CADASTRAR
    if opcao == "1":
        print("Por favor, informe seus Dados.\n")
        nome_c = input("Nome: ") 
        data_n = input("Data de nascimento: ")
        cpf_c = input("CPF: ")
        for i in range(0, len(clientes)):
            if clientes[i]['cpf'] == cpf_c:
                cpf_dup ="Este CPF já está cadastrado."
                print(cpf_dup)
                
        if cpf_dup == "Este CPF já está cadastrado.":
            break

        logradouro = input("Logradouro: ")
        nro = input("Número: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        sig_estado = input("Sigla do Estado: ")
        cad_cliente(nome_c, data_n, cpf_c, logradouro, nro, bairro, cidade, sig_estado)
        print(clientes)

    # OPÇÃO SAIR
    elif opcao == "3":
         break
    
    


"""while True:
    
    opcao = input(menu_op)
    
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        print(depositar(valor, saldo, extrato))
            
    elif opcao == "s":
        
        if lim_saque > num_saque:
            lim_saque -=1
            valor = float(input("Informe o valor do saque: "))
            
            print(sacar(valor, sal=saldo, ext=extrato))
                
        else:
            print("***Operação falhou! Você atingiu o número maximo de saques diários.***")
            
    elif opcao =="e":
        print(f_extrato(ext=extrato))
             
    elif opcao == "q":
        break
        
    else:
        print("***Opção Inválida.***")"""
