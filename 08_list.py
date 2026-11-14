import os
os.system("clear")                  

                    # LISTAS
# Sequencia de elementos de varios tipos
# print("\nCriar lsitas")
# lista_num = [1, 2, 3, 4, 5]
# lista_fruta = ["maça", "bananas", "pera"]
# lista_mix = [1, "ola", 3.14, True]
# lista_vazia =[]
# lista_de_listas = [[1, 2],[3, 4]]
# matrix = [[1, 2], [3, 4], [5, 6]]

# print("\nAcesso a elementos por indice")
# print(lista_fruta[0])           #maça
# print(lista_fruta[-1])          #ultimo da lita (pera)
# print(lista_de_listas[1][0])    #3


                    # SLICING DE LISTAS
# Usar so determinada parte da lista

# lista_num = [1, 2, 3, 4, 5]
# print(lista_num[1:4])           # imprime do elemento 1 ate ao 4-1(3)
# print(lista_num[:3])            # imprime do 0 ao 3-1(2)
# print(lista_num[3:])            # imprime da posiçao 3 ate ao fim 
# print(lista_num[:])             # copia da lista total

# lista[desde:ate:passo]

lista_num = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista_num[::2])               # para devolver indices pares, de 2 em 2
print(lista_num[::-1])              # devolve a lista do fim para o principio


                    # MODIFICAR LISTA
lista_num[0] = 20                   # altera a primeira posiçao da lista
lista_num[120] = 20                 # erro fora de rango, pq q lista nao tem posiçao 120

                    # ADICIONAR ELEMENTOS NA LISTA
lista_num1 = [1, 2, 3]
lista_num1 = lista_num1 + [4, 5, 6]
lista_num1 += [7, 8, 9]                 # forma mais curta e eficiente

                    # SABER TAMANHO DE UMA LISTA
print("\nSaber tamanho da lista")
len(lista_num1)