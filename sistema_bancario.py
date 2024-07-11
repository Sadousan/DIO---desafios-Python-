import re
from datetime import datetime

# Desafio de código do bootcamp Python da DIO. Deve-se criar um programa básico com 3 funcionalidades: Saque, depósito e extrato.

saldo = 0
extrato = []
cont = 0

def sacar(valor):
    global saldo
    global cont

    if valor > saldo:
        print(f'Saldo insuficiente para saque.\nValor disponível: {saldo:.2f}')
    elif valor > 500 or cont >= 3:
        print(f'\nVocê só pode sacar 3 valores diários de até R$ 500.\n')
    else:
        saldo -= valor
        cont += 1
        saque_formatado = f'\nSaque realizado com sucesso.\nSaldo disponível ainda: {saldo:.2f}'
        extrato.append({"data_hora": datetime.now(), "tipo": "Saque", "valor": valor, "saldo": saldo})
        print(saque_formatado)

def depositar(valor):
    global saldo

    if valor <= 0:
        print("Valor inválido para depósito. Digite um valor positivo.\n")
    else:
        saldo += valor
        deposito_formatado = f'\nDeposito realizado com sucesso.\nSaldo ainda disponível: {saldo:.2f}'
        extrato.append({"data_hora": datetime.now(), "tipo": "Depósito", "valor": valor, "saldo": saldo})
        print(deposito_formatado)
    
def gerar_extrato():
    if not extrato:
        return "\nNenhum extrato encontrado."

    extrato_formatado = f"\nExtrato:\n"
    for i, operacao in enumerate(extrato):
        data_hora = operacao["data_hora"].strftime("%d/%m/%Y %H:%M:%S")
        tipo = operacao["tipo"]
        valor = operacao["valor"]
        saldo = operacao["saldo"]
        extrato_formatado += f"{i+1}: {data_hora} - {tipo}: R$ {valor:.2f} - Saldo: R$ {saldo:.2f}\n"

    return extrato_formatado

def main():
    while True:
        nome = input("\n»Digite seu nome completo: ")
        if not re.match(r"^[a-zA-Z]+(?: [a-zA-Z]+)*$", nome) or len(nome) < 3:
            print("Nome inválido. Apenas letras são permitidas.")
        else:
            break

    margem_menu = nome.split()[0].center(44, '_')
    menu = f'''
        {margem_menu}
            
        1 - Sacar
        2 - Depositar
        3 - Extrato
        4 - Sair
        
        {margem_menu}'''

    while True:
        print(menu)
        try:
            opcao = int(input("\n»Digite a opção desejada: "))
        except ValueError:
            print("\nOpção inválida. Digite um número inteiro.\n")
            continue

        if opcao == 1:
            try:
                valor = float(input("Digite o valor para sacar: "))
                sacar(valor)
            except ValueError:
                print("\nValor inválido. Digite um número.\n")
            continue

        elif opcao == 2:
            try:
                valor = float(input("Digite o valor para depositar: "))
                depositar(valor)
            except ValueError:
                print("\nValor inválido. Digite um número.\n")
            continue

        elif opcao == 3:
            print(f"\nGerando extrado de {nome} ...")
            print(gerar_extrato())

        elif opcao == 4:
            print("\nSaindo do programa...")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")

main()
