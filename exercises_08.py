import os
os.system("clear")  

# --------------------------- FUNCTIONS ------------------------------


                   # Exercicio 1: Imprimir números del 1 a 10
# Imprime os números de 1 al 10 (inclusive) usando loop for e range().
def print_num(a, b):
    print(f"Os numeros entre {a} e {b}:")
    for num in range(a, b + 1):
        print(num)

print_num(1, 10)



                    # Exercicio 2: Imprimir números impares de 1 a 20
# Imprime todos os números impares entre 1 y 20 (inclusive) usando loop for e range().
def impares(a, b):
    print(f"Os numeros impares entre {a} e {b}:")
    for num in range(a, b + 1, 2):
            print(num)
    
impares(1, 20)



                    # Exercicio 3: Imprimir múltiplos de 5
# Imprime os múltiplos de 5 desde 5 ate 50 (inclusive) usando loop for e range().
def multiplos(a, b, multp):  
    print(f"Os multiplos de {multp}, entre {a} e {b}:")
    for num in range(a, b + 1, multp):
      print(num)

multiplos(a=5, b=50, multp=5)



                    # Exercicio 4: Imprimir números em orden inversa
# Imprime os números de 10 al 1 (inclusive) em orden inversa usando loop for e range().
def inversa(a, b):
    print(f"A contagem inversa entre {a} e {b}")
    for num in range(b, a, -1):
        print(num)

inversa(1, 10)



                    # Exercicio 5: Soma de números em um rango
# Calcula la soma dos números de 1 al 100 (inclusive) usando loop for y range().
def soma_total(a, b):
    total = 0
    
    for num in range(a, b + 1):
        total += num
    print(f"O valor total da soma dos numeros entre {a} e {b} = {total}")

soma_total(1, 100)



                    # Exercicio 6: Tabuada com numero inserido pelo user
# Imprime a tabuada de esse número (del 1 al 10) usando loop for y range().
# numero = int(input("Insira o numero que deseja ver a sua tabuada completa: "))
def tabuada(a):
    total = 0
    print(f"Tabuada do {a}")
    for num in range(1, 11):
        total = a * num
        print(f"{a} x {num} = {total}")

tabuada(2)
        
       
