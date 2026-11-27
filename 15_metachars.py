                    # META CARACTERES
    # Sao simbolos especiais com significados especificos nas expressoes regulares



    # (.) - coincidir com qualquer caracter exepto uma nova linha. um . é so um caracter
import re
text = "Ola mundo, OLa de novo, O$a outra vez"
pattern = "O.a"

found = re.findall(pattern, text)
if found:
    print(found)
else:
    print("Nao encontrado")                     # encontra as 3x Ola


    # Para utilizar conforme as normas: r para criar um RAW String
import re
text = "Ola mundo, OLa de novo, O$a outra vez"
pattern = r"O.a"                                # usar r antes da cadeia de texto

found = re.findall(pattern, text)
if found:
    print(found)
else:
    print("Nao encontrado")                  



    # (\) - ignora sgnificado especial de um simbolo
import re
text = "A minha casa é branca. A minha prancha é amarela."
pattern = r"\."                                              # ignora significado especial do ponto . e procura precisamento o ponto final
# pattern = r"."                                             # sem a barra, so com o ponto, vai encontrar todas as letras e todso so espaços 

match = re.findall(pattern, text)
print(match)



    # (\d) coincide com qualquer digito (0-9)
import re
text = "O numero de telefone é: 123456789"
found = re.findall(r"\d", text)
print(found)                        # R= ['1', '2', '3', '4', '5', '6', '7', '8', '9']

import re
text = "O numero de telefone é: 123456789"
found = re.findall(r"\d\d\d", text)
print(found)                        # R= ['123', '456', '789']

import re
text = "O numero de telefone é: 123456789"
found = re.findall(r"\d{9}", text)  # {9} significa que tem um tamanho de 9 numeros
print(found)                        # R= ['123456789']


    # (\w) Coincide con qualquer caracter alfanumerico (bom metodo para ver email)
import re
text = "Tiago_Costa_88_€"
pattern = r"\w"
found = re.findall(pattern,text)
print(found)                                # Nao encontra o € pq nao é alfanumerico.


    # (\s) Coincide com qualquer espaço em branco (espaço, tab, salto de linha)
import re
text = "Ola\nComo estas?\t"
pattern = r"\s"
match = re.findall(pattern,text)
print(match)                                # ['\n', ' ', '\t']


    # (^) Coincide com o principio de uma cadeia.
import re
username = "@321_name"
patterns = r"^\w"                # validadar nome de usuario

valid = re.search(pattern, username)
if valid: print("Usuario Valido")
else: print("Nome de usuario nao é valido")

    # ---------------------- Outro Exemplo ----------------------------
phone = "+351 912345678"
pattern = r"^\+\d{2,3} "            # espaço em branco no final indica que depois do indicativo deve ter um espaço

valid = re.search(pattern, phone)
if valid: print("Numero Valido")
else: print("Numero nao é valido")


    # ($) Validar final da cadeia
text = "Ola mundo."
pattern = r"mundo$"                 # tem que terminar em mundo     - se terminar em mundo. ja nao é valido

valid = re.search(pattern, text)
if valid: print("Texto Valido")
else: print("Texto nao valido ")



    # (\b) Coincide o principio e o final de uma palavra
text = "casa casada cosa cosas casado casa"
pattern = r"\bc.sa\b"

found = re.findall(pattern, text)
print(found)


    # (|) Coincid con una opción u otra
fruits = "platano, piña, manzana, aguacate, palta, pera, aguacate, aguacate"
pattern = r"palta|aguacate|p..a|\b\w{7}\b"

matches = re.findall(pattern, fruits)
print(matches)






