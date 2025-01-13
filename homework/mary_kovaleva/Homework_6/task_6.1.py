text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
words = text.split()
text2 = []
for word in words:
    if word.endswith((',', '.')):
        word = word[:-1] + 'ing' + word[-1]
        text2.append(word)
    else:
        text2.append(word + 'ing')
print(" ".join(text2))
