
def to_boolean_list(word):
    return [(ord(c) - 96) % 2 == 1 for c in word]

