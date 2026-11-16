                    # Loop (while)
        # Permitem executar um bloco de codigo enquanto se cumpra uma condiçao
        # contar, procurar, filtrar...

import os
os.system("clear") 

# print("\nLoop while")
# contador = 0
# while contador <= 5:
#     print(contador)
#     contador +=1        # importante para evitar loop infinito


# while True:
#     print("Ola")        # loop infinito pq nunca passa a False


        # Para parar um loop podemos usar um break

# print("\nLoop while com 'break'")       # break faz sair do loop
# contador = 0
# while True:
#     print(contador)
#     contador +=1 
#     if contador == 5:
#         break               # ao entrar na condiçao 5 para o ciclo (break)


# print("\nLoop while com 'continue'")        # continue faz com que continue o loop
# contador = 0
# while contador < 10:
#     contador +=1 

#     if contador % 2 == 0:
#         continue                            # se entra neste loop volta ao inicio do loop while. nao executa o codigo seguinte
        
# print(contador)


# print("\nLoop while com 'else'")            # se tiver break dentro, nunca executa o else
# contador = 0
# while contador < 5:
#     print(contador)
#     contador +=1 
# else:                                       # interessante para saber se a condiçao passou a ser falsa.                 
#     print("Ciclo terminado")                # quando nao cumpre a condiçao do while, entra no else



                    # Exercicio

        # Nesta resposta, se o utilizador insere uma letra, o programa da erro.
# numero = -1
# while numero <= 0:
#     numero = int(input("Indroduz um numero positivo: "))
#     if numero < 0:
#         print("O numero deve ser positivo")
# print(f"O numero que introduziste é = {numero}")


                # try execpt : tenta executar o try. Se nao corresponder, salta para o execpt
# numero = -1
# while numero <= 0:
#     try:
#         numero = int(input("Indroduz um numero positivo: "))
#         if numero < 0:
#            print("O numero deve ser positivo")
#     except:
#         print("O que introduzes deve ser um numero")
        
# print(f"O numero que introduziste é = {numero}")