
def get_middle(word):
    if len(word) % 2 == 0:
        return word[len(word) // 2 - 1:len(word) // 2 + 1]
    return word[len(word) // 2:len(word) // 2 + 1]

