import random

def generate_password(lenght, chars):
    result = ''
    new_chars = []
    new_chars.extend(chars)
    random.shuffle(new_chars)
    for _ in range(lenght):
        result += new_chars[random.randint(0, len(new_chars) - 1)]
    return result

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

number_password = int(input('Сколько паролей нужно сгенерировать? '))
password_len = int(input('Длина пароля? '))

answer = input("Включать ли цифры '0123456789' (Д или Н)? ")
enable_digits = answer.lower() == 'д'

answer = input("Включать ли прописные буквы 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' (Д или Н)? ")
enable_uppercase = answer.lower() == 'д'

answer = input("Включать ли строчные буквы 'abcdefghijklmnopqrstuvwxyz' (Д или Н)? ")
enable_lowercase = answer.lower() == 'д'

answer = input("Включать ли символы '!#$%&*+-=?@^_' (Д или Н)? ")
enable_punctuation = answer.lower() == 'д'

answer = input("Исключать ли неоднозначные символы 'il1Lo0O' (Д или Н)? ")
disable_controversial = answer.lower() == 'д'

if enable_digits:
    chars = chars + digits
if enable_lowercase:
    chars = chars + lowercase_letters
if enable_uppercase:
    chars = chars + uppercase_letters
if enable_punctuation:
    chars = chars + punctuation
if disable_controversial:
    for ch in 'il1Lo0O':
        chars.replace(ch, '')

passwords = []
for _ in range(number_password):
   passwords.append(generate_password(password_len, chars))
print(*passwords, sep='\n')
