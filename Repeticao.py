"""
#FOR
texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
  if letra.upper() in VOGAIS:
    print(letra, end=" ")
"""

"""
#função range
for numero in range(0,11):
  print(numero, end=" ")
  """

"""
#WHILE
opcao = -1
while opcao != 0:
  opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

  if opcao == 1:
    print("sacando...")
  elif opcao == 2:
    print("exibindo o extrato...")
else:
  print("Fim")
"""

"""
while True:
  numero = int(input("Informe um número: "))

  if numero == 10:
    break
#break para quebrar o laço
  print(numero)
"""
"""
for numero in range(100):
  if numero == 12:
    break

  print(numero, end=" ")
"""
"""  
for numero in range(10):
  if numero == 2:
    continue
#continue para pular o número ou condição
  print(numero, end=" ")
  """
"""
for numero in range(20):
  if numero % 2 != 0:
    continue
#continue para pular o número ou condição
  print(numero, end=" ")  
  """

while True:
  numero = int(input("Informe um número: "))

  if numero == 10:
    break

  if numero % 2 == 0:
    continue

  print(numero)