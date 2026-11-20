"""
Objetivo: 4 Fantasticos
Criar uma funçao que receba um grupo de texto.
Esta funçao deve contar quantas vezes aparece 'R' e quantas vees aparece 'J'.
- Se a quantidade de R e de J sao iguais: A Funçao deve returnar True
- Se as quantidades nao sao iguais: A funçao retorna False
- No caso de nao aparecer nenhuma vez as letras (0 = 0): Funçao retorna True
"""

def check_balance(text):
    text = text.upper()         # tranformar tudo em maiusculas

    count_r = text.count("R")
    count_j = text.count("J")

    print(f"J: {count_j}, R: {count_r}")

    # if count_r == count_j:    # metodo longo. tentar nao fazer
    #     return True
    # else:
    #     return False

    return count_r == count_j   # mesmo resultado, menos codigo

print(check_balance("RRJJ"))
print(check_balance("RRRRJJ"))
print(check_balance("RRJJJJJ"))
print(check_balance("aaAAaaAfbsfvsdvg"))