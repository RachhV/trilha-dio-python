"""MAIOR_IDADE = 18

idade = int(input("informe a sua idade: "))

if idade >= MAIOR_IDADE:
  print("Maior de idade")

if idade < MAIOR_IDADE:
  print("Menor de idade")
"""

"""MAIOR_IDADE = 18

idade = int(input("informe a sua idade: "))

if idade >= MAIOR_IDADE:
  print("Maior de idade")

else:
  print("Menor de idade")
"""

#cinema valores de entrada
"""LIMITE_IDADE = 18
IDADE_ESPECIAL = 70

idade = int(input("informe a sua idade: "))

if idade <= LIMITE_IDADE:
  print("Paga meia")

elif idade >= IDADE_ESPECIAL:
  print("Meia idoso")

else:
  print("Valor integral")
"""

"""conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
  if saldo >= saque:
    print("saque realizado com sucesso.")
  
  elif saque <= (saldo + cheque_especial):
    print("saque realizado com cheque especial")

  else:
    print("saldo insuficiente")

elif conta_universitaria:
  if saldo >= saque:
    print("saque realizado com sucesso.")
  else:
    print("saldo insuficiente")

else:
  print("erro no sistema")
  """


#estrutura condicional ternaria
saldo = 2000
saque = 500
status = "sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque!")
