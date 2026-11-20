                    # DICIONARIOS
        # Colecçoes de pares key-value para armazenar dados
import os
os.system("clear") 


    # Exemplo tipico de dicionario:
pessoa = {
    "nome": "Tiago",
    "idade": 38,
    "estudante": True,
    "classific": [9, 12, 10],
    "trabalhador": True,
    "social": {                             # dicionario dentro de um dicionario
        "instagram": "@t.costa",
        "github": "tiagofdcosta"
    }
}

    # para aceder aos dados
print("\nImprimir Dados")
print(pessoa["nome"])
print(pessoa["classific"][2])          # key = classific, na posiçao 2
print(pessoa["social"]["github"])

    # mudar valores
pessoa["nome"] = "Tiago Costa"
pessoa["classific"][0] = 11

print(pessoa)                           # imprimir todo o dicionario

    # eliminar completamente uma propriedade
del pessoa["idade"]
print(pessoa)

    # eliminar mas poder guardar numa variavel
e_estudante = pessoa.pop("estudante")       # guardou o valor numa variavel, mas eliminou do dicionario
print(f"É estudante? {e_estudante}")
print(pessoa)

    #update de valores, um dicionario com outro diciobario
a = {"nome": "Tiago", "age": 38 }
b = {"nome": "Tiago Costa", "e_estudante": True}

a.update(b)                     # atualiza os valores da a com os parametros da b (nao elimina nada que ja estava na a)
print(a)

    # verificar se existe uma propriedade (True or False)
print("name" in pessoa)     # False
print("nome" in pessoa)     # True


    # obter todas as keys
print("\nKeys:")
print(pessoa.keys())

    # obter todos os Values
print("\nValues:")
print(pessoa.values())

    # obter key e value -> guarde em tuple
print("\nItems (key and Value, Tuple):")
print(pessoa.items())

for key, value in pessoa.items():
    print(f"{key}: {value}")

# -------------------------------------  PARTE 2 -----------------------------------------

                     # Criar dicionario 
program_dict = {
    "Bug": "An error in a program.",
    "Function": "A piece of code.",
}

                    # Imprimir value
print(program_dict["Function"])                       # nome_dicionario["key"]    ->  colocar key para sair value


                     # Adicionar items 
program_dict["Loop"] = "The action of doing."         # nome_dicionario["key"] = "alue"


                     # Esvaziar Dicionario. Existe mas fica vazio
program_dict = {}
print(program_dict)


                    # Editar values
program_dict["Bug"] = "A moth in your computer."
print(program_dict)

                    # Imprimir todas as keys existentes no dicionario
for key in program_dict:
    print(key)
    print(program_dict[key])



                #Dicionarios Paises : Capitais
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

                  # Listas dentro de Dicionarios
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])
#
                        # Dicionario dentro de dicionario
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
print(travel_log["Germany"]["cities_visited"][2])

  

                #listas de Contactos
lista_contactos = {
    "Tiago": "tiagocosta€gmail.com",
    "Ines": "inesdias@gmail.com",
    "cenas": "cenas@gmail.com",
    "anonimo": "anonymous€hotmail.com"
                }

print(lista_contactos.keys())                                                     #imprime todas as keys, em lista
print(lista_contactos.values())                                                   #impreme todas as values , em lista
lista_contactos["Benardo"] = "grandapalerma@facebook.com"                         #Adicionar na lista
print(lista_contactos.items())

                         # Verificar se um contacto esta na lista. Procurar pela key
for nome in lista_contactos:
    if nome == "Tiago":
        print(f"{nome} está na lista!")

for key, value in lista_contactos.items():
    if value == "tiagocosta@gmail.com":
        print(value, "->", key)


                    # Dicionario com Numeros

a_list = [10, 20, 30]
b_list = [4, 5, 6]
c_list = [2020, 2023, 2026]

dictionary = {
    "dias": a_list,
    "meses": b_list, 
    "anos": c_list,
    "seculos": {"meses": 12, 
                "semanas": 450,
                 "dias": 2500 }
    }

print("\nVerificar pela key se existe no dicionario ou nao:")
if "dias" in dictionary:
    print("'dias' está no Dicionario")
else:
    print("Nao esta no dicionario")

print("\nVerificar pelo value se existe no dicionario ou nao:")
if 10 in dictionary["dias"]:
    print("10 está no Dicionario")
else:
    print("10 Nao esta no dicionario")


print("\nEnumerate, start no indice 0")
for x in enumerate(dictionary):                 # enumera o indice de cada uma das keys
    print(x)                                    
                    # Resultado:
                    # (0, 'dias')
                    # (1, 'meses')
                    # (2, 'anos')
                    # (3, 'seculos')

print("\nEnumerate, start no indice 1")
for x in enumerate(dictionary, start=1):                 # start=1 indica que o primeiro indice = 1 e nao = 0
    print(x)                                    
                    # Resultado:
                    # (1, 'dias')
                    # (2, 'meses')
                    # (3, 'anos')
                    # (4, 'seculos')

print("\nEnumerate, imprimir indices")
for x, y in enumerate(dictionary):                
    print(x)                                     # enumera os indices do dicionario
                    # Resultado:
                    # 0 
                    # 1
                    # 2
                    # 3

print("\nEnumerate, imprimir keys do dicionario")
for x, y in enumerate(dictionary):                
    print(y)                                       # enumera keys do dicionario
                        # Resultado:
                        # dias
                        # meses
                        # anos
                        # seculos

print("\nEnumerate.values()")
for x in enumerate(dictionary.values()):                
    print(x) 
                        # Resultado:
                        # (0, [10, 20, 30])
                        # (1, [4, 5, 6])
                        # (2, [2020, 2023, 2026])
                        # (3, {'meses': 12, 'semanas': 450, 'dias': 2500})

print("\nEnumerate.items()")
for x in enumerate(dictionary.items()):                 
    print(x)
                        # Resultado:
                        # (0, ('dias', [10, 20, 30]))
                        # (1, ('meses', [4, 5, 6]))
                        # (2, ('anos', [2020, 2023, 2026]))
                        # (3, ('seculos', {'meses': 12, 'semanas': 450, 'dias': 2500}))

print("\nDicionario.keys()")
for key in dictionary.keys():                   # acesso as keys do dicionario
    print(key)

print("\nDicionario.values()")                  
for value in dictionary.values():               # acesso as values do dicionario
    print(value)

print("\nDicionario.items()")
for key, values in dictionary.items():          # acesso as keys e values do dicionario
    print(key, values)




                            # ----------- EXERCICIO -------------
    # Student Grades Exerc (day 9)
# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
# # Classificar cada aluno
student_grades = {}
for student in student_scores:                               # Loop para ver todas as keys
    score = student_scores[student]                           # ver os values associados a cada key
    print(student)
            # Verificaçao de grades
    if score >= 91:
            student_grades[student] = 'Outstanding'
    elif score >= 81:
            student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

print(student_grades)

#Students with above > 80
for key, value in student_scores.items():
    if value > 80:
        print(f"{key}: {value}", "(more than 80)")

for key, value in student_scores.items():
    print(value)
