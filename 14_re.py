                    # RegEX_ Expressoes Regulares
""" Sao uma sequencia de caracteres que formam um padrao de busca.
Utilizam-se para fazer buscas de cadeias de texto, validaçao de dados, etc...

Servem Para:
- busca avançada: encontrar padroes especificos em textos grandes de forma rapida e precisa;
- validaçao de dados: asegurar que os dados sao correctos
- manipulaçao do texto: Extrair, modificar... cadeias de texto facilmente
"""

        # 1. Importar modulo de RegEX
import re       

        # 2. Criar um padra. cadeia de texto que descreve o que queremos encontrar
pattern = "Ola"

        # 3. O texto onde queremos pesqueisar a palavra
text = "Ola mundo"

        # .search()     Usar a funçao de busca de "re"
result = re.search(pattern, text)               # result é tipo Match   |   Vai procurao no pattern, o text |   None: se nao encontra    
if result:
    print("Encontrei o padrao de texto")
else:
    print("Nao encontrei padrao de texto")

        # .group()  devolve a cadeia de texto que coincide com o padrao
result.group()
print(result.group())                           # Ola


        # .start() devolve a posiçao inicial
print(result.start())                           # Posiçao 0


        # .end() devolve a posiçao final
print(result.end())                             # Posiçao 3 (":posiçao 0, O:posiçao 1, l:posiçao 2, a:posiçao 3")


        # .findall()    Encontrar todas as coincidencias de um patrao (aparece varias vezes no text)
text = "Gosto de Python. Python é uma maravilha. Python nao é muito dificil"

pattern = "Python"
matches = re.findall(pattern, text)                 # devolve uma lista das vezes que encontrou
print(matches)                                      # ['Python', 'Python', 'Python']


        # encontrar todas mesmo sem ser com a palvra exatamente igual
text = "Gosto de Pyhhon. Python é uma maravilha. Python nao é muito dificil"

pattern = "Py.hon"                                  # o . indica que nessa posiçao pode ter kk letra. tem de iniciar em Py "kk letra" hon          
matches = re.findall(pattern, text)                 # devolve uma lista das vezes que encontrou
print(matches)                                      # ['Pyhhon', 'Python', 'Python']


        # Ver quantas vezes encontrou a palavra
text = "Gosto de Python. Python é uma maravilha. Python nao é muito dificil"
pattern = "Python"
matches = re.findall(pattern, text)                 # devolve uma lista das vezes que encontrou
print(len(matches))                                 # 3


        # iter() devolve um iterador que contem todos os resultados da busca
text = "Gosto de Python. Python é uma maravilha. Python nao é muito dificil"

pattern = "Python"
matches = re.finditer(pattern, text)                

for match in matches:
    print(match.group(), match.start(), match.end())
                                                        # Resposta:
                                                        # Python 9 15
                                                        # Python 17 23
                                                        # Python 41 47


                    # Modificadores
    # Opçoes qe se podem agregar aos padroes para mudar o seu comportamento

        # re.IGNORECASE: Ignora as maiusculas e minusculas

text = "Todo o mudo diz que a ia vai-nos tirar trabalho. Mas a IA nao é assim tao ma. Viva a Ia"
pattern = "IA"                                
found_ia = re.search(pattern, text, re.IGNORECASE)                      # re.IGNORECASE
if found_ia:
    print(f"Encontrei o padrao de texto na posiçao {found_ia.start()} e termina na posiçao {found_ia.end()}")
else:
    print("Nao encontrei o padrao de texto")



text = "Todo o mudo diz que a ia vai-nos tirar trabalho. Mas a IA nao é assim tao ma. Viva a Ia"
pattern = "IA"                                
found = re.findall(pattern, text, re.IGNORECASE)                      # re.IGNORECASE
if found:
    print(found)                                                      # detecta IA, ia e Ia



                # .sub() Substituir texto
        # substitui todas as coincidencias de um padrao num texto
import re
text = "Ola mundo. Ola de novo"
pattern = "Ola"
replacement = "Adeus"

new_text = re.sub(pattern, replacement, text)
print(new_text)