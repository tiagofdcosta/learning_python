                    #   QUANTIFIERS, Quantificadores
    #   Utilizam-se para especificar quantas ocorrencias de um caracter ou grupo de caracteres se devem encontrar numa cadeia de texto

import re

    # (*) pode aparecer 0 ou mais vezes
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)


    # (+) verifica se aparece 1 ou mais vezes
text = "bbbb aaa cc d aa casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)                                      # ['aaa', 'aa', 'a', 'a']


    # (?) 0 ou 1 vez
    # EXEMPLO: Quantas palavras tens de 0 ou mais "a" y depois 1 "b"
text = "aaabacb"
pattern = r"a?b"
matches = re.findall(pattern, text)
print(matches) 


    # {n} aparece exetamete n vezes
text = "aaaaaa      aa      aaaa"
pattern = r"a{3}"
matches = re.findall(pattern, text)
print(matches) 


    # {n, n} de n a n vezes
text = "b bb bbb b"
pattern = r"b{2,3}"
matches = re.findall(pattern, text)
print(matches) 




