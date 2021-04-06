
def rotated_words(txt):
    result = set()
    for word in txt.split():
        can_be_rotated = True
        for letter in word:
            if letter not in ["H", "I", "N", "O", "S", "X", "Z", "W"]:
                can_be_rotated = False
                break
        if can_be_rotated:
            result.add(word)
    return len(result)

