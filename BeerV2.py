def func():
    first = input('первое слово: ')
    second = input('второе слово: ')
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
    return ' '.join(words)


print(func())
