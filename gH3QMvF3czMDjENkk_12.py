
def remove_letters(letters, word):
​
    lst_1 = list(word)
​
    for x in range(len(lst_1)):
        if lst_1[x] in letters:
            y = letters.index(lst_1[x])
            del letters[y]
            continue
​
    return letters

