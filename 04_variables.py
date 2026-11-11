                    # VARIAVEIS

# my_name = "Tiago"
# print(my_name)

# age = 38
# print(age)

# TIPO DINAMICO: o tipo de dado de determina em tempo de execuçao.
                # Nao tem de ser decalrado esplicitamente:

# name = "Tiago" 
# print(type(name))       # str

# name = 10
# print(type(name))       # int


# TIPO FORTE: python nao mistura tipo incopativeis. 
# Nao raliza conversoes de tipo em automatico

#print(10 + "2")     # TypeError

# F-STRINGS (cadeia de formato) - misturar tipos diferentes
my_name = "Tiago"
age = 30
print(f"Ola {my_name}, tenho {age + 5} anos")