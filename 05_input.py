                    # INPUT
# Entradas de usuario. Permite ao utilizador inserir dados atraves da consola.

# nome = input("Ola, como te chamas?\n")
# print(f"Ola {nome}, prazer em conhocer-te")

# age = int(input("Que idade tens?\n"))
# print(f"Daqui a 20 anos terás {age + 20}")

print("Obter multiplas variaveis")
country, city = input("Em que pais e cidade?\n").split()      #split() faz associaas respostar a cada uma das variaveis no mesmo input. Input deve ser separado por espaços
print(f"Vives em {country}, {city}")