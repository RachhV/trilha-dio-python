"""
curso = "     PytHOn  "

print(curso.upper())
print(curso.lower())
print(curso.title())

#remover espaços em branco
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())
"""
"""
curso = "Python"
print(curso.center(10, "#"))
#ou seja, você quer que tenha 10 caracteres, deixando a palavra no meio e preenchendo o #
#se não informar, será espaço em branco

print("-".join(curso))
#para intercalar as letras
"""
"""
# INTERPOLAÇÃO DE VARIÁVEIS
#old style %
nome = "Raquel"
idade = 25
profissão = "programadora"
linguagem = "Python"
print("Olá, me chamo %s. Tenho %s anos, trabalho como %s e estou estudando %s." % (nome, idade, profissão, linguagem))

#format
print( "Olá, me chamo {}. Tenho {} anos, trabalho como {} e estou estudando {}." .format(nome, idade, profissão, linguagem))
print("Olá, me chamo {3}. Tenho {2} anos, trabalho como {1} e estou estudando {0}." .format(linguagem, profissão, idade, nome))
print("Olá, me chamo {nome}. Tenho {idade} anos, trabalho como {profissao} e estou estudando {linguagem}.".format)
##uso de dicionário .format(**pessoa)

#fstring
print(f"Olá, me chamo {nome}. Tenho {idade} anos, trabalho como {profissão} e estou estudando {linguagem}.")

PI = 3.14159
print(f"Valor de PI: {PI: .2f}")

# FATIAMENTO
nome = "Raquel Fraga Veiga"
print(nome[0])
print(nome[:6])
#lembrar que começa no 0 e o final é excluido (então adicionar +1)
print(nome[7:13])
print(nome[:]) #tudo
print(nome[::-1]) #espelhamento
print(nome[-1]) #última letra
"""

# STRING MULTIPLAS LINHAS
nome = "Raquel"
mensagem = f'''Olá meu nome é {nome},
              estou aprendendo Python.
      essa mensagem tem diferentes recuos.'''
print(mensagem)