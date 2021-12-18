import string
import random


def pass_gen():

    string_lower = string.ascii_lowercase
    string_upper = string.ascii_uppercase
    string_digits = string.digits
    string_punctuation = string.punctuation

    # lista vazia
    pass_list = []

    # adiciona os caracteres à lista
    pass_list.extend(string_lower)
    pass_list.extend(string_upper)
    pass_list.extend(string_digits)
    pass_list.extend(string_punctuation)

    # embaralha os caracteres da lista(reorganiza a ordem dos itens da lista)
    random.shuffle(pass_list)

    # obter o comprimento da senha a partir da entrada do utilizador
    pass_length = int(input("Insira o comprimento (tamanho) da senha : "))

    # converter a lista de palavras-passe em cadeia do índice
    # 0 para o comprimento da palavra-passe introduzida pelo utilizador
    password_result = "".join(pass_list[0:pass_length])

    # imprimir palavra-passe gerada
    print("A senha gerada é : ", password_result)


pass_gen()