import os
os.system("clear") 

"""
2 litas com o mesmo tamanho
- Se o número na lista_a e maior, o seu valor soma-se ao siguinte número da lista_a.
- Se o número na lista_b e maior, o seu valor soma-se ao siguinte número da lista_b.
- Se os dois números sao iguais, ambos se eliminam e nao afectan o siguinte par.

Deves simular esta comparaçao e devolver o resultado final:
- Se no final sobra um número na lista_a, devolve esse número seguido da letra "a" (ex: 3a)
- Se no final sobra um número na lista_b, devolve esse número seguido da letra "b" (ex: 1b)
- Em caso de empate, devolve a letra "x".
"""

def battle(lista_a, lista_b):
    pontos_a = sum(lista_a)
    pontos_b = sum(lista_b)
    if pontos_a > pontos_b:
        return f"{pontos_a - pontos_b}a"
    elif pontos_b > pontos_a:
        return f"{pontos_b-pontos_a}b"
    else:
        return "x"

lista_a = [2, 4, 4]
lista_b = [2, 8, 2]
winner = battle(lista_a, lista_b)
print(winner)



