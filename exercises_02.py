import os
os.system("clear")

                    # Exercicio 1: Determinar o numero maior
# Pede ao usuario para introduzir dois numero, depois imprime indicando qual é o maior ou se sao iguais:

# print("\nVamos verificar qual o maior de dois numeros")
# n1 = float(input("Por favor diz-me o primeiro numero: "))
# n2 = float(input("Agora o segundo numero: "))

# if n1 == n2:
#     print("Os numeros sao iguais")
# elif n1 > n2:
#     print(f"O primeiro numero({n1}) é maior que o segundo({n2})")
# else:
#     print(f"O segundo numero({n2}) é maior que o primeiro({n1})")



                    # Exercicio 2: Calculadora simple
# Pede ao usuario 2 numero e uma operaçao (+, -, *, /)
# Realizara o operaçao e verifica a divisao por zero)

# print("\nVamos fazer calculo entre dois numeros ")
# operacao = input("Qual a operaçao que queres fazer entre esses numeros? (+, -, *, /) ")
# n1 = float(input("Por favor diz-me o primeiro numero: "))
# n2 = float(input("Agora o segundo numero: "))

# if operacao == "+":
#     soma = n1 + n2
#     print(f"A soma entre os dois numeros é = {soma}")

# if operacao == "-":
#     subtracao = n1 - n2
#     print(f"A subtraçao entre os dois numeros é = {subtracao}")

# if operacao == "*":
#     multip = n1 * n2
#     print(f"A multiplicaçao entre os dois numeros é = {multip}")

# if operacao == "/":
#     if n2 == 0:
#         print("Erro: ZeroDivisionError")
#     else:
#         div = n1 / n2
#         print(f"A divisao os dois numeros é = {div}")



                    # Exercicio 3: Ano bisexto
# Pedir ao usuario para introduzir um ano e determinar se é bissexto
# Um ano e bissexto se for divisivel por 4, exepto se é divisivel por 100 mas nao por 400.

# print("\nVamos verificar se o ano é bissexto ")
# ano = int(input("Por favor diz-me o ano a verificar: "))

# if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
#     print(f"O ano {ano} é bissexto")
# else:
#     print(f"O ano {ano} nao é bissexto")



                    # Exercicio 4: Categorizar idades
# Pede ao usuario uma idade e depois vamos categoriza-la
# - Bebé (0-2 anos)
# - Miudo (3-12 anos)
# - Adolescente (13-17 anos)
# - Adulto (18-64 anos)
# - Cotinha (65 anos ou mais)

# print("\nVamos categorizar por idades")
# idade = int(input("Qual a idade: "))

# if idade >= 0 and idade <= 2:
#     print(f"Com {idade} anos é considerado Bebé")
# elif idade >= 3 and idade <= 12:
#     print(f"Com {idade} anos é considerado Miudo")
# elif idade >= 13 and idade <= 17:
#     print(f"Com {idade} anos é considerado Adolescente")
# elif idade >= 18 and idade <= 64:
#     print(f"Com {idade} anos é considerado Adulto")
# else:
#     print(f"Com {idade} anos é considerado Cotinha")