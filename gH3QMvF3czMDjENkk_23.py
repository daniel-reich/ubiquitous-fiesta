
def remove_letters(letters, word):
    for i in range(len(word)):
        for j in range(len(letters)):
            if word[i] == letters[j]:
                del letters[j]
                break
    return letters

