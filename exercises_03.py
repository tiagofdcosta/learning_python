
import os
os.system("clear")   

                    # Exercicio 1: Mensagem Secreta
# Utilizando slicing e concatenaçao, cria uma lista que tenha so a mensagem "secreto"

# mensagem = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# secreto = mensagem[7:]
# print(secreto)


                    # Exercicio 2: Mudanças de Posiçoes
# Mudar a primeira e a ultima posiçao usando indices.
# numeros = [10, 20, 30, 40, 50]
# numeros[0], numeros[-1] = numeros[-1], numeros[0]
# print(numeros)


                    # Exercicio 3: Sándwich de listas
# Criar uma lista chamada sandwich que contenha o pao em cima, ingredientes e pao em baixo (nesta ordem).
# pao = ["pao de cima"]
# ingredientes = ["jamón", "queijo", "tomate"]
# pao_baixo = ["pao de baixo"]

# sandwich = pao + ingredientes + pao_baixo
# print(sandwich)



                    # Exercicio 4: Duplicando a lista
# Criar uma nova lista que contenha os elementos da lista origina duplicados.
# lista = [1, 2, 3]
# lista_duplicada = lista + lista
# print(lista_duplicada)


                     # Exercicio 5: Extraindo o centro
# Dada uma lista com um número impar de elementos, extrair o elemento que se encontra no centro da lista (utilizando slicing)
# lista = [10, 20, 30, 40, 50]
# print(lista[2])
                    # OU
# centro = len(lista) // 2
# print(lista[centro])


                    # Exercicio 6: Reversa parcial
# Dada una lista, invierte a primeira metada utilizando slicing e concatenación).
# Exemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
# lista = [1, 2, 3, 4, 5, 6]
# lista1 = lista[0:3]
# lista2 = lista[3:6]
# lista1_inv= (lista1[::-1])
# lista_final = lista1_inv + lista2
# print(lista_final)

                    # OU
# metade = len(lista) // 2
# meia_lista = lista[0:metade]
# metade_invertida = meia_lista[::-1]
# lista_final = metade_invertida + lista[metade:]
# print(lista_final)
