string_1 = input('Введите 1-ую строку: ').strip().replace('  ', ' ').split(' ')
string_2 = input('Введите 2-ую строку: ').strip().replace('  ', ' ').split(' ')

new_mas = []

index_from_string2 = 1
i = 0
length_string2 = len(string_2)

while length_string2 != 0:
    string_1.insert(index_from_string2, string_2[i])
    i += 1
    index_from_string2 += 2
    length_string2 -= 1

print('Строка в шахматном порядке: ', ' '.join(string_1))
