# Вывести последнюю букву в слове

word = 'Архангельск'
# Можно так    print (f'Последняя буква: {last_letter}')
# Можно так    print (f'Последняя буква: {word[10]}')
print (f'Последняя буква: {word[-1]}')

# Вывести количество букв "а" в слове
a = 0
for letter_a in word.lower():
    if letter_a == 'а':
        a += 1
print (f'Количество букв "a" в слове: {a}')

# Вывести количество гласных букв в слове

vowel = 0
for letter_vowel in word.lower():
    if letter_vowel == 'а' or letter_vowel == 'о' or letter_vowel == 'э' or letter_vowel == 'у' or letter_vowel == 'ы' or letter_vowel == 'я' or letter_vowel == 'ё' or letter_vowel == 'е' or letter_vowel == 'ы' or letter_vowel == 'и':
        vowel += 1
print (f'Количество гласных букв: {vowel}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(f'Количество слов в предложении "Мы приехали в гости": {len(sentence.split())}')

# Вывести первую букву каждого слова на отдельной строке
letter_first = 0
print('Первая буква каждого слова на отдельной строке:')
for letter_first in sentence.split():
    print(letter_first[0])

# Вывести усреднённую длину слова.
sum_lenght = 0
for lenght in sentence.split():
    sum_lenght += len(lenght)
print(f'Усреднённая длина слова: {sum_lenght/len(sentence.split())}')
