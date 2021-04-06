
add_letters = lambda a: chr((sum(ord(x) - 96 for x in a) - 1) % 26 + 97)

