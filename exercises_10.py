import re

                    # Exercicio 1
""" Encontra a primeira ocorrencia da palavra IA no seguinte texto, e indica em que posicao termina."""

text = "Todo o mudo diz que a IA vai-nos tirar trabalho."

pattern = "IA"                                  # se procurarmos em minusculas, ja nao encontra
found_ia = re.search(pattern, text)
if found_ia:
    print(f"Encontrei o padrao de texto na posiçao {found_ia.start()} e termina na posiçao {found_ia.end()}")
else:
    print("Nao encontrei o padrao de texto")



                    # Exercicio 2
""" 
1. Encontra todas as ocorrencias da palavra 'Tiago' no texto seguinte.
2. Indica a posiçao onde termina e onde acaba.
3. Quantas vezes se encontrará.
"""

text = "Tiago esta a estudar Python. O Primeiro e ultimo nome sao Tiago Costa"
word = "Tiago"

    # 1. Encontra todas as ocorrencias da palavra 'Tiago' no texto seguinte.
    # 2. Indica a posiçao onde termina e onde acaba.
matches = re.finditer(word, text)
for match in matches:
    print(f"{match.group()}, começa em {match.start()} e acaba em {match.end()}")
   

    # 3. Quantas vezes se encontrará.
matches = re.findall(word, text)
print(f"Encontrei a palavra {word} {len(matches)} vezes.")



                    # Exercicio 2
""" 
1. Encontra todas as ocorrencias da palavra 'Tiago' no texto seguinte.
Ignorar mauisculas e minusculas
"""
import re
text = "Tiago esta a estudar Python. O Primeiro e ultimo nome sao TIAGO COSTA A pagina de GitHub é tiagofdcosta"
word = "Tiago"
found = re.findall(word, text, re.IGNORECASE)
if found:
    print(found)