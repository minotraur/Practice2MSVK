# def func():  # Консольный вид
#     first = input('первое слово: ')
#     second = input('второе слово: ')
#     line = "Васе сегодня в ларёк не завезли пиво"
#     words = line.split(' ')
#     some_word = None
#     some_word2 = None
#     for i, word in enumerate(words):
#         if word.startswith(first):
#             some_word = word
#             del words[i]
#             break
#
#     for i, word in enumerate(words):
#         if word.startswith(second):
#             some_word2 = word
#             del words[i]
#             break
#
#     words.insert(0, some_word)
#     words.insert(1, some_word2)
#     return ' '.join(words)
#
#
# print(func())

from tkinter import *


def func(event):
    first = first_word_ent.get()
    second = second_word_ent.get()
    line = "Васе сегодня в ларёк не завезли пиво"
    words = line.split(' ')
    some_word = None
    some_word2 = None
    for i, word in enumerate(words):
        if word.startswith(first):
            some_word = word
            del words[i]
            break

    for i, word in enumerate(words):
        if word.startswith(second):
            some_word2 = word
            del words[i]
            break

    words.insert(0, some_word)
    words.insert(1, some_word2)

    lab['text'] = ' '.join(words)


root = Tk()

label = Label(text='Васе сегодня в ларёк не завезли пиво', font=14)
first_word_ent = Entry(width=40)
second_word_ent = Entry(width=40)
but = Button(text='Преобразовать', font=14)
lab = Label(width=40, bg='black', fg='white', font=14)

but.bind('<Button-1>', func)

label.pack(side=TOP)
first_word_ent.pack(side=LEFT)
second_word_ent.pack(side=RIGHT)
but.pack()
lab.pack(side=BOTTOM)

root.mainloop()
