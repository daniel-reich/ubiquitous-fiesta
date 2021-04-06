
def index_of_caps(word):
    position = 0
    newlist = []
    for letter in word:
        if letter.isupper():
            newlist.append(position)
        position += 1
    return newlist

