words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def multiply_words(*kwargs):
    for k, v in kwargs[0].items():
        print(k * v)


multiply_words(words)
