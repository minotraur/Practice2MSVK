from text_to_num import text2num
from enchant.checker import SpellChecker


def int_to_Roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


checker = True

while checker:
    try:
        word = input('Введите число на английском языке: ')
        number = text2num(word, 'en')
        checker = False
    except ValueError:
        checker = SpellChecker("en_US")
        checker.set_text(word)
        print('Ошибка в слове: ' + ' '.join([i.word for i in checker]))

print(f'Число переведённое с английского - {number}.\nЧисло в римской системе - {int_to_Roman(number)}.')
