
def hangman(phrase, lst):
    phrase = list(phrase)
    for i in range(len(phrase)):
        if phrase[i].isalpha() and phrase[i] != ' ' and (phrase[i].lower() not in lst and phrase[i].upper() not in lst):
            phrase[i] = '-'
    return ''.join(phrase)

