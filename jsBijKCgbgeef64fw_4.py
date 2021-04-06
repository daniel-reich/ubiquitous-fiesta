
def wumbo(words):
    wumbo_sentence = []
    for letter in words:
        if letter == 'M':
            wumbo_sentence.append('W')
        else:
            wumbo_sentence.append(letter)
    return ''.join(wumbo_sentence)

