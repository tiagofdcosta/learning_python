import os
os.system("clear")    

                    # Exercicio 1: Adicionar e modificar elementos
         # Criar uma lista com os numeros de 1 a 5
lista_num = [1, 2, 3, 4, 5]
print(lista_num)

         # Adiciona 6 no final da lista usando append()
lista_num.append(6)
print(lista_num)

         # Inserir o 10 na posiçao 2 com insert()
lista_num.insert(2, 10)
print(lista_num)

         # Modifica o primeiro elemento da lista para que seja 0
lista_num[0] = 0
print(lista_num)



                    # Exercicio 2: Combinar e Limpar listas
         # Criar 2 listas:
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
        # Extende a lista_a com lista_b usando extend().
lista_a.extend(lista_b)
print(lista_a)

     # Elimina a primera vez que aparece o 1 na lista_a usando remove().
lista_a.remove(1)
print(lista_a)

     # Elimina o elemento no índice 3 de lista_a usando pop(). Imprime o que foi eliminado.
apagado = lista_a.pop(3)
print(f"O elemento apagado foi: {apagado} que estava na posiçao 3")

     # Limpa completamente lista_b usando clear().
lista_b.clear()
print(f"lista b = {lista_b}")


                    # Exercicio 3: Slicing e Eliminaçao do del.
     # Criar uma lista  com os elementos de 1 a 10
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Utiliza slicing e del para eliminar os elementos desde o índice 2 ate ao 5 (sen incluir 5).
del lista[2:5] 
print(lista)


                     # Ejercicio 4: Ordenar y contar
lista = [5, 2, 8, 1, 9, 4, 2]
         # Ordena a lista de forma ascendente usando sort().
print(lista.sort())

         # conta quantas vezes aparece o número 2 na lista usando count().
print(lista.count(2))

         # verifica se o número 7 está na lista usando in.
print(7 in lista)


                    # Exercicio 5: Copia vs. Referencia
lista = [1, 2, 3]

         # Cria uma copia da lista chamada copia_1 , usando slicing.
copia_1 = lista[:]
print(f"A lista copiada com o nome copia_1 = {copia_1}")

        # Cria otra copia chamada copia_2 usando copy()
copia_2 = lista.copy()
print(f"A lista copia_2 = {copia_2}")

        # Cria uma referencia a lista original chamada referencia.
referencia = lista
print(f"Referencia = {referencia}")

        # Modifica o primero elemento de la lista referencia a 10.
referencia[0] = 10
print(f"Referencia com primeiro elemento alterado = {referencia}")

        # Imprime as 4 listas (lista, copia_1, copia_2, referencia) e observa as alteraçoes.
print(lista)
print(copia_1)
print(copia_2)
print(referencia)



                    # Exercicio 5: Ordenar strings sem diferenciar maiúsculas y minúsculas.
fruits = ["Manzana", "pera", "ananas", "BANANA", "naranja"]

        # Ordena a lista sen diferenciar entre maiúsculas y minúsculas.
fruits.sort(key=str.lower)
print(f"A lista ordenada, ignuranto Maisculas e minusculas = {fruits}")



