
def move(word):
    new_word = ''
    for i in word:
        new_word = new_word + chr(ord(i) + 1)
    return new_word

