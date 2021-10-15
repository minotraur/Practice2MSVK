from text_to_num import text2num
from spellchecker import SpellChecker


def int_to_roman(num):
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
        word = input('Введите число на французском языке: ').lower()
        number = text2num(word, "fr")
        checker = False
    except ValueError:
        checker = SpellChecker(language='fr')
        correct_word = checker.correction(word)
        print(f'Ошибка в слове {word}, возможно вы имели ввиду: {correct_word}?')

print(f'Число переведённое с английского - {number}.\nЧисло в римской системе - {int_to_roman(number)}.')
