menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

saldo = 0
limite_saques = 3
extrato = []

def depositar(saldo):
    valor = int(input("informe o valor: "))

    if valor <= 0:
        print("Digite um valor positivo.")
        extrato.append('Erro ao depositar.')
    else:
        saldo += valor
        print(f'Saldo atual: R${saldo:.2f}')
        extrato.append(f'Depositou: {valor:.2f}')
    
    return saldo

def sacar(saldo, limite_saques):
    valor = int(input("informe o valor: "))
    
    if valor > 500: 
        print("Escolha um valor até R$500")
        extrato.append('Erro ao sacar.')
    else:
        if valor > saldo:
            print("Saldo insuficiente.")
            extrato.append('Erro ao sacar.')
        else:
            saldo -= valor
            limite_saques -= 1
            print(f'Sacou: R${valor}   Saldo atual: R${saldo}   Saques restantes hoje:{limite_saques}')
            extrato.append(f'Sacou: {valor:.2f}')

    return saldo, limite_saques


while True:
    opcao = input(menu)

    if opcao == 'd':
        saldo = depositar(saldo)

    elif opcao == 's':
        if limite_saques != 0:
            saldo, limite_saques = sacar(saldo, limite_saques)     
        else:
            print("Limite de saque excedido.")

    elif opcao == 'e':
        print(f'Saldo atual: R${saldo:.2f}')
        for item in extrato:
            print(item)

    elif opcao == 'q':
        break

    else:
        print("Comando invalidado.")