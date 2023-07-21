
menu = """
    OPERAÇÕES:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
lim_saque = 3
val_max_saque = 500
extrato = ""
num_saque = 0

def cad_usuario():
    return

def cad_conta_bancaria():
    return

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

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        print(depositar(valor, sal=saldo, ext=extrato))
            
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
        print("***Opção Inválida.***")
