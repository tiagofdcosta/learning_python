import os
os.system("clear")  

                    # Exercicio 1: Imprimir números pares
        # Imprime todos os números pares de 2 a 20 (inclusive) usando ciclo for.
for number in range(2, 21):
    if number % 2 == 0:
        print(number)



                    # Exercicio 2: Calcular a media da lista
numeros = [10, 20, 30, 40, 50]
total = 0
for num in numeros:
    total += num
media = total / len(numeros)
print(f"A media = {media}")



                    # Exercicio 3: Buscar o máximo de uma lista
numeros = [15, 5, 25, 10, 20]
max = 0
for num in numeros:
    if num > max:
        max = num
print(f"O numero maior da lista = {max}")



                    # Exercicio 4: Filtrar cadeias por longitude
        # Criar uma nova lista que tenha so as palavras con mais de 5 letras
        # usando un bucle for y list comprehension.
palavras = ["casa", "copo", "sol", "elefante", "gaiola", "gato"]
for palavra in palavras:
    if len(palavra) > 5:
        print(palavra)                                                           # nao imprimi uma lista, so as palavras


palavras = ["casa", "copo", "sol", "elefante", "gaiola", "gato"]
palavras_grandes = [palavra for palavra in palavras if len(palavra) > 5]         # imprime em lista
print(palavras_grandes)



                    # Exercicio 5: Contar palavras que comecem com uma letra indicada pelo user
        # Conta quantas palavras na lista começam com essa letra (sem diferenciar maiúsculas/minúsculas).
palavras = ["casa", "arvore", "sol", "elefante", "armario", "lua", "carro"]
contador = 0
letra = input("Quer uma palavra que comece por que letra? ").lower()
for palavra in palavras:
    if palavra.lower().startswith(letra):                                     # startswitch(letra)    verifica a primea letra da palavra
        palavra_certa = palavra
        contador += 1
print(f"Existe {contador} palavras iniciadas por {letra}.")