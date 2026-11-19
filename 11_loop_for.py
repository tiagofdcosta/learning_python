                    # Loop (for)
    
# print("\nLoop For")
# frutas = ["maça", "pera", "tangerina", "melancia"]
# for fruta in frutas:
#     print(fruta)


# cadeia = "tiago"
# for caracter in cadeia:
#     print(caracter)


            # enumerate()   ->  permite devolvero numero do indice
# frutas = ["maça", "pera", "tangerina", "melancia"]
# for index, fruta in enumerate(frutas):
#     print(f"O indice (key) e {index} e o valor (value) e {fruta}")


            # loop aninhados ( ciclos for dentro de ciclos for)
# letras = ["A", "B", "C"]
# numeros = [1, 2]
# for letra in letras:
#     for numero in numeros:
#         print(f"{letra}{numero}")



            # loop com break    -   para o loop ao encontrar o break
# print("\nBreak")
# animais = ["gato", "cao", "piriquito", "urso"]
# for index, animal in enumerate(animais):
#     print(animal)
#     if animal == "gato":
#         print(f"O gato esta na posiçao = {index}")
#         break


            # loop com continue 
# print("\nContinue")            
# animais = ["gato", "cao", "piriquito", "urso"]
# for index, animal in enumerate(animais):
#     if animal == "gato":
#         continue                                # ao encontrar o gato salta o loop e nao imprime
#     print(animal)


            # list comprehension
animais = ["gato", "cao", "piriquito", "urso"]
        # meter letras maiusculas em todos os animais
animais_maisuc = [animal.upper() for animal in animais]
print(animais_maisuc)


            # list comprehension com uma condiçao if
num_pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(num_pares)



            # range -    NAO CRIA LISTA. Permite criar uma sequencia de numero
# print("\nRange")
# for num in range(10):              # nao cria uma lista!
#     print(num)

# for num in range(5, 10):           # de 5 a 9
#     print(num)

# for num in range(0, 10, 2):        # de 0 a 9 em passos de 2
#     print(num)

# for num in range(-5, 0):        
#     print(num)

# for num in range(10, 0, -1): 
#     print(num)


            # Criar lista com range     list()
# nums = range(10)
# list_of_numbs = list(nums)
# print(list_of_numbs)


            # Repetir algo 5 vezes
# for _ in range(5):
#     print("Imprimir 5x")