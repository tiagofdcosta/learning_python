                    # IF 
# Condiçoes IF, ELIF, ELSE: Permitem executar blocos de codigo so se cumprirem com determinadas condiçoes

import os
os.system("clear")               # Limpat terminal cada vez que correr o programa


# print("\nCondiçao simples, if")
# age = 18

# if age >= 18:
#     print("Es maior de idade")
#     print("Felicidades")


# print("\nCondiçao simples com else")
# age = 18
# if age >= 18:
#     print("Es maior de idade")
# else:
#     print("Menor de idade")


# print("\nCondiçao simples com elif")        # So cumpre uma das condiçoes
# nota_aluno = 7
# if nota_aluno >= 10:
#     print("Qualificado")
# elif nota_aluno >= 17:
#     print("Exelente")
# else:                                       # Nao e obrigatorio ter else. Pode nao ter.
#     print("Chumbado")


# print("Condiçoes Multiplas")
# age = 20
# carta_conduçao = True

# if age >= 18 and carta_conduçao:            # se uma das condiçoes é falta, resultado é falsa
#     print("Podes Conduzir")
# else:
#     print("Policia!")

# if age >= 18 or carta_conduçao:              # se pelo menos uma das condiçoes é verdadeira, resultado é verdadeiro
#     print("Podes Conduzir")
# else:
#     print("Policia!")

# fim_de_semana = False 
# if not fim_de_semana:
#     print("tens de faturar")



        # Nao aconselhavem, mas possivel
# print("if dentro de if")
# age = 18
# tens_dinheiro = True

# if age >= 18:
#     if tens_dinheiro:
#         print("Podes ir a discoteca")
#     else:
#         print("fica em casa")
# else:
#     print("Nao podes entrar na discoteca")

        # Mais pratico e facil
# if age < 18:
#     print("Nao podes ir a disco")
# elif tens_dinheiro:
#     print("Podes ir a disco")
# else:
#     print("Fica em casa")


# numero = 5
# if numero:          #True
#     print("O numero nao é zero")

# numero = 0
# if numero:          #False
#     print("Nao entra pq if é False")

# nome = ""
# if nome:            #False
#     print("Nao entra porque o nome esta vazio")


                    #CONDIÇAO TERNARIA
# Forma concisa de un if-else numa so linha
# [codigo se cumpre a condiçao] if[condiçao] else[codigo se nao cumpre]

idade = 15
msg = "maior de idade" if idade >= 18 else "menor de idade"



# print("I´ll say you a bigger number in the next 5 ones")
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a next one: "))
# num3 = int(input("Enter a next one: "))
# num4 = int(input("Enter a next one: "))
# num5 = int(input("Enter a last one: "))

# bigger_number = ""
# if num1 > num2:
#     print(f"Bigger number is = {num1}")
# elif num2 > num3:
#     print(f"Bigger number is = {num2}")
# elif num3 > num4:
#     print(f"Bigger number is = {num3}")
# elif num4 > num5:
#     print(f"Bigger number is = {num4}")
# else:
#     print(f"Bigger number is = {num5}")