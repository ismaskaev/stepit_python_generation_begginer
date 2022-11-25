def caesar_cipher():
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

def len_of_word(word):
    word_len = 0
    for i in range(len(word)):
        ch = word[i]
        if not ch.isalpha():
            continue
        word_len += 1
    return word_len

def caesar_cipher_advanced(text):
    new_text = ''
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_alphabet = upper_alphabet.lower()

    word_list = text.split(' ')

    for word in word_list:
        step = len_of_word(word)

        for i in range(len(word)):
            ch = word[i]
            if not ch.isalpha():
                new_text += ch
                continue

            if ch.isupper():
                alphabet = upper_alphabet
            else:
                alphabet = lower_alphabet
            index = alphabet.find(ch)
            if index == -1:
                new_text += ch
                continue
            new_index = (index + step) % len(alphabet)
            new_text  += alphabet[new_index]

        new_text += ' '
    return new_text.strip()

phrase = input('Введите исходную фразу: ')
print(caesar_cipher_advanced(phrase))