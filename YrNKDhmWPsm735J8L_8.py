
def sort_word(word):
    return ''.join(sorted(word)) if word != word.upper() else ''.join(sorted(word[0:]))

