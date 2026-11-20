"""
Dado um array de numeros e um numero 'goal', encontra os 2 primeiros numeros do array que somem o numero goal y devolve os seus indices.
Se nao existir tal combinaçao, devolve None
nums = [4, 5, 6, 2]
goal = 8
find_first_sum(nums, goal)  # [2, 3]
"""
import os
os.system("clear") 

                # WITH FOR

# def find_first_num(nums, goal):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):       # 2 ciclos for devem ser evitados. Usar dicionarios
#             if nums[i] + nums[j] == goal:
#                 return [i, j]
#     return None                                 # Nao se encontra combinaçao

                


                # WITH DICTIONARIES

def find_first_num(nums, goal):
    """Procura dois numeros da list cuja soma seja igual a goal. Quando encontra um par, devolve os indices desses numeros"""
    dicionario_item = {}

    for indice, value in enumerate(nums):
        print(f"{indice}: {value}")
        num_falta = goal - value     
        print(num_falta)               # goal = 8
        if num_falta in dicionario_item:
            print(dicionario_item[num_falta])
            return [dicionario_item[num_falta], indice]
        dicionario_item[value] = indice  
        # print(value, indice)              # guardar o numero atual no dicionario pq nao encontramos a combinaçao
    return None


nums = [4, 5, 6, 2]
goal = 8
result = find_first_num(nums, goal)
print(result)