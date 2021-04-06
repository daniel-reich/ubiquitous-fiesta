
def to_boolean_list(word):
    return [(ord(i) + 1) % 2 == 0 for i in word]

