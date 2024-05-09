
menu = """""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)
  
  if opcao == "d":
    valor = float(input("Informe o valor do depósito: "))
    
    if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor: .2f}\n"
    
    else:
      print("Erro. O valor informado é inválido.")

  elif opcao == "s":
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print("Não há saldo suficiente para a operação.")
      
    elif excedeu_limite:
      print("O valor do saque excede o limite por operação.")

    elif excedeu_saques:
      print("Não é possível fazer mais do que três saques diários.")

    elif valor > 0:
      saldo -= valor
      extrato += f"Saque: R$ {valor: .2f}\n"
      numero_saques += 1 

    else:
      print("Erro. O valor informado é inválido.")


  elif opcao == "e":
    e = "EXTRATO"
    print(e.center(20, "="))
    print("Não foram realizadas transações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")


  elif opcao == "q":
    break 

  else:
    print("Operação inválida, selecione a operação desejada: ")
