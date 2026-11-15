
                    # METODOS EM LISTAS
import os
os.system("clear") 

# lista = ["a", "b", "c", "d"]

                # ADICIONAR ELEMENTO NA LISTA
# lista.append("e")                            # adiciona no fim da lista
# print(lista)

# lista.insert(1, "@")                        # insere elemento na posiçao que indicamos (1)
# print(lista) 

# lista.extend(["nadar", "correr"])           # adiciona elementos ao final da lista
# print(lista)


                #ELIMINAR ELEMENTOS DA LISTA
# lista.remove("a")                          # eliminar o primeiro (a neste caso) que aparece na lista (nao pagada todos, so o primeiro)
# print(lista)

# ultimo = lista.pop()                       # eliminar ultimo elemento da lista e devolve-o (pode-se guardar numa variavel)
# print(ultimo)
# print(lista)

# lista.pop(1)                                 # elimina o elemento que esta na posiçao indicada (1)
# print(lista)

# lista.clear()                                   # eliminar todos os elementos da lista
# print(lista)  

# del lista[1:3]                                 # sintaxe para eliminar items num determinado rango (neste casa o indice 3 ainda aparece)
# print(lista)

# del lista[3:]                                  # elimina items da posiçao 3 ate ao fim
# print(lista)

                    # ORDENAR LISTA
# print("\nOrdenar numeros modificando a lista original")
# numbers = [120, 34, 12, 7, 15, 23]
# numbers.sort()                                                   #ordena a lista por ordem ascendente. modifica a lista e nao se pode guardar como nova variavel
# print(numbers)

# print("\nOrdenar numeros criando uma copia")
# numbers = [120, 34, 12, 7, 15, 23]
# sorted_numbers = sorted(numbers)                                   #copia da lista com os elementos ordenados. a lista original mantem-se
# print(sorted_numbers)

# print("\nOrdenar textos criando uma copia (letras minusculas)")
# frutas = ["limao", "banana", "pera", "melancia", "ananas"]          # se tiver letras maiusculas, maiusculas vem primeiro
# sorted_frutas = sorted(frutas)
# print(sorted_frutas)

# print("\nOrdenar textos criando uma copia (mistura de minisculas com maiusculas)")
# frutas = ["Limao", "banana", "pera", "Melancia", "ananas"]  
# frutas.sort(key=str.lower)                                             # a key faz com que todas as letras sejam consideradas minusculas


                            # OUTROS METODOS UTEIS
# numeros = [7, 12, 45, 7, 90, 62]
# print(numeros.count(7))                                                # conta o quantas vezes um elemento se repete na lista

# print(54 in numeros)                                                  # verifica se algum elemento esta na lista. devolve True ou False

# copia_numeros = numeros[:]                                              # copia toda a lista creando outra variavel
# print(numeros)
# print(copia_numeros)

# lista_copia = numeros.copy()                                             # Copiar lista para nova lista utilizando copy()
# print(f"A lista copia chamada lista_copia = {lista_copia}")