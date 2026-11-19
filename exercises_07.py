import os
os.system("clear")  


                   # Exercicio 1: Imprimir números del 1 a 10
    # Imprime os números de 1 al 10 (inclusive) usando loop for e range().
for numb in range(1, 11):
    print(numb)


                    # Exercicio 2: Imprimir números impares de 1 a 20
    # Imprime todos os números impares entre 1 y 20 (inclusive) usando loop for e range().
for numb in range(1, 21, 2):
    print(numb)


                    # Exercicio 3: Imprimir múltiplos de 5
    # Imprime os múltiplos de 5 desde 5 ate 50 (inclusive) usando loop for e range().
for num in range(5, 51, 5):
    print(num)


                    # Exercicio 4: Imprimir números em orden inversa
    # Imprime os números de 10 al 1 (inclusive) em orden inversa usando loop for e range().
for num in range(10, 0, -1):
    print(num)


                    # Exercicio 5: Soma de números em um rango
    # Calcula la soma dos números de 1 al 100 (inclusive) usando loop for y range().
total = 0
for num in range(1, 101):
    total += num
print(f"A soma de todos os numeros = {total}")



                    # Exercicio 6: Tabuada com numero inserido pelo user
    # Imprime a tabuada de esse número (del 1 al 10) usando loop for y range().
numero = int(input("Insira o numero que deseja ver a sua tabuada completa: "))
total = 0
for num in range(1, 11):
    total = numero * num
    print(f"{numero} * {num} = {total}")


                    # Exercicio 7: 
    # Usuario insere texto.
    # Verificar se aparece determinada letra, escolhida pelo usuario.
texto = ""
print("\nVerificar quantas vezes aparece determinada letra")
texto = input("Insita uma palavra ou frase: ")
letra = input("Qual a letra que deseja contar? ").lower()
contagem = 0
for x in texto:
    if x == letra:
        contagem += 1
print(f"A letra {letra} aparece -> {contagem} vezes")