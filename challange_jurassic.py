"""
No filme Jurassic Park, observa-se que os dinossauros carnivoros, como o T-Rex, depositam um numero par de ovos.
Imagina que tens uma lista de numeros inteiros em que cada numero representa a quantidade de ovos postos por um dinossauro.

Importante: So se considera os ovos de dinossauros carnivores (T-Rex), aqueles numeros que sao pares.

Objetivo:
Escrever uma funçao que receba a lista de numeros inteiros e devolva a soma total de todos os ovos que pertencem a dinossauros carnivoros,
ou seja, a soma de todos os numeros pares da lista.
"""

def count_carnivore_din_eggs(eggs_list) -> int:     # -> int indica o tipo de info
    """
    Esta funçao recebe a lista de numeros de inteiros que representam a quantidade de ovos meteram diferentes dinossauros e os numeros par sao carnivosros.
    Devolve um numero com a soma de todos os ovos dos carnivoros
    """
    total_carnivore_eggs = 0

    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_eggs += eggs

    return total_carnivore_eggs

egg_list = [3, 4, 7, 5, 8]
print(count_carnivore_din_eggs(egg_list))

