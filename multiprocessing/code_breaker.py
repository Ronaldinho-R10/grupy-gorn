import random
import string
import multiprocessing

# Função para gerar um código de comprimento especificado
def generate_code(length):
    charset = string.ascii_letters
    code = ''.join(random.choice(charset) for _ in range(length))
    return code

# Função para gerar uma string com padrão específico
def generate_string(_):  # Adicionamos um argumento, mas não o usamos
    number_s = str(random.randint(1, 5))
    string_part = ''.join(random.choice(string.ascii_uppercase) + number_s for _ in range(4))
    return string_part

def main():
    num_codes = 5

    with multiprocessing.Pool() as pool:
        codes = pool.map(generate_code, [11] * num_codes)
        strings = pool.map(generate_string, range(num_codes))

    for code in codes:
        print(code.upper())

    for string_part in strings:
        print(string_part)

if __name__ == '__main__':
    main()