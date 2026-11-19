                    # Funçoes
            # Blocos de codigo reutilizaveis e parametrizaveis para fazer farefas especificas

"""Definiçao de uma funçao

def nome_da_funçao(parametro1, parametro2, ...):
    # docstring
    # comentarios
    return valor de retorno (opcional)

"""

        # Exemplo de funçao sem parametro
# def cumprimentar():
#     print("Ola")

# cumprimentar()
# cumprimentar()


        # Exemplo com parametros
# def cumprimentar_a(nome):           # nome = parametros
#     print(f"Ola {nome}")

# cumprimentar_a("Tiago")               # Tiago = argumento 


#         # funçoes com mais parametros
# def somar(a, b):
#     soma = a + b
#     return soma

# result = somar (2, 3)
# print(result)


#         # Documentar funçao com docstring
# def subtraçao(a, b):
#     """Subtrai dois numeros e devolve resultado"""
#     return a - b

# print(subtraçao.__doc__)        # printa no ecran a documentaçao da definiçao

# help(subtraçao)                 # limpa terminal e mosta a ajuda da funçao selecionada


        # Parametros por defeito
# def multiplicar(a, b = 2):          # valor a variavel, valor b fixo
#     return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))


#         # Argumento por posiçao
# def descrever_pessoa(nome, idade, sexo):
#     print(f"Sou {nome}, tenho {idade} anos e me idenfifico como {sexo}")

# descrever_pessoa("Tiago", 38, "masculino")


#         # Argumento por key, parametros com nome
# descrever_pessoa(sexo ="masculino", idade = 38, nome = "Tiago")


        # Argumentos de longitude de variavel (*args)
# def somar_numeros(*args):
#     soma = 0
#     for numeros in args:
#         soma += numeros
#     return soma

# print(somar_numeros(1, 2, 3, 4, 5, 6, 7))



            # Argumentos com key-value variavel (**kwargs)
def mostrar_info_de(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

mostrar_info_de(nome="Tiago",idade= 38, sexo="masculino", gatos=True)
print("\n")
mostrar_info_de(name="Ines", age=39, cats=3, city="Damaia")