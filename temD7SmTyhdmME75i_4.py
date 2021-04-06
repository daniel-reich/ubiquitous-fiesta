
def to_boolean_list(word):
    return [bool((ord(c) - 96) % 2) for c in word]

