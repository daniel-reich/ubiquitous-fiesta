
def move(word):
    return "".join([chr(bytes(char, 'utf-8')[0] + 1) for char in word])

