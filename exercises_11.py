                    # EXERCICIO
    # Detectar se ha um numero de Portugal num texto com o prefixo +351

import re
text = "O meu numero de telefone +351 912345678. Guarda-o!"
pattern = r"\+351 \d{9}"                # \+ para ignorar o significado espscial do +. Assim procura mesmo o sinal +
                                        # \d representa um algarismo; {9} indica que são esperados exatamente nove
found = re.search(pattern, text)        # re.search(pattern, text) procura a primeira ocorrência desse padrão em text. Devolve um objeto se encontrar uma correspondência, ou None se não encontrar.

if found:
    print(f"Encontrei o num telefone: {found.group()}")
else:
    print("Nao encontrei")