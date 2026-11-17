import os
os.system("clear")


                   # Exercicio 1: Conte descendente
        # Imprime os números de 10 a 1 usando um loop while
num = 10
print(num)
while num >= 1:
    print(f" numero = {num}")
    num -= 1
    
    

                    # Exercicio 2: Soma de números pares (while)
        # Calcula a soma dos números pares entre 1 e 20 (inclusive) usando un loop while.
num = 1
soma_pares = 0
while num <= 20:
    if num % 2 == 0:
        soma_pares += num
    num += 1
print(f"Soma dos numeros par = {soma_pares}")
    


                    # Exercicio 3: Factorial de um número
        # Pede ao usuario que introduza um número inteiro positivo.
        # Calcula o seu factorial usando loop while.
        # O factorial de um número inteiro positivo e o producto de todos os números 1 a esse número. 
        # Ex: el factorial de 5     ->      5! = 5 x 4 x 3 x 2 x 1 = 120.
factorial = 1
contador = 1
print("Factorial de um numero inserido pelo User")
num = int(input("Introduza um numero inteiro positivo: "))
while num >= contador:
    factorial *= contador
    contador += 1
print(f"Factorial de {num} = {factorial}")


                    # Exercicio 4: Validaçao de password
        # Pede ao usuario que introduza uma password. Deve ter pelo menos 8 caracteres.
        # Usa um loop while para seguir pedindo a password ate que cumpra com os requisitos.
        # Se a password e válida, imprime "Password válida".
print("\nCriar Passaword com 8 caracteres")
tamanho_pass = 0

while tamanho_pass < 8:
    password = input("Introduza Passaword com 8 caracteres: ")
    tamanho_pass = len(password) 
    if tamanho_pass < 8 :
        print("A Password deve ter pelo menos 8 caracteres")
    else:
        print("Password Valida")


                    # Exercicio 5: Tabuada
        # Pede al usuario que introduza un número.
        # Imprime la tabela de multiplicar de esse número (de 1 a 10) usando un loop while.

print("\nTabela de Multiplicaçao")
mult = 1
total = 0
num = int(input("Introduza um numero para mostrar a tabuada: "))

while mult <= 10:
    total = num * mult
    print(f"{num} * {mult} = {total}")
    mult += 1



                    # Exercicio 6: Números primos ate N
    # Pede al usuario que introduza un número inteiro positivo N.
    # Imprime todos os números primos menores ou iguais que N usando un loop while.
numero = 2
while numero <= n:
  es_primo = True                                   # assumimos que o número e primo ate que se demonstre o contrario
  divisor = 2
  while divisor * divisor <= numero:                
    if numero % divisor == 0:
      es_primo = False                              # Sie encontramos um divisor, nao e primo
      break                                         # Saimos do loop interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1



                    # Exercicio 7: Count up to N — Ask for a number N, then print from 1 to N.
        # print("\nImprimir numeros de 1 ate ao numero escolhido pelo User")
n = int(input("Insira um numero: "))
num = 0
while num < (n + 1):
    print (num)
    num += 1
