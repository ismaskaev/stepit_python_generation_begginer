print('Выберите режим наботы:', '1. Зашифровать', '2. Дешифровать', sep='\n')
mode = int(input('Режим работы: '))
print('Выберите язык:', '1. RU', '2. ENG', sep='\n')
lang = int(input('Язык: '))
phrase = input('Введите исходную фразу: ')

if lang == 1:
    upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
elif lang == 2:
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
else:
    pass

lower_alphabet = upper_alphabet.lower()
alf_len = len(upper_alphabet)

step = int(input('Укажите шаг сдвига: '))
print()

new_phrase = ''
step = step % alf_len
for i in range(len(phrase)):
    ch = phrase[i]
    if not ch.isalpha():
        new_phrase += ch
        continue
    if ch.isupper():
        index = upper_alphabet.index(ch)
        if mode == 1:
            new_index = (index + step) % alf_len
        else:
            new_index = (index - step) % alf_len
        new_phrase += upper_alphabet[new_index]
    else:
        index = lower_alphabet.index(ch)
        if mode == 1:
            new_index = (index + step) % alf_len
        else:
            new_index = (index - step) % alf_len
        new_phrase += lower_alphabet[new_index]

print(new_phrase)