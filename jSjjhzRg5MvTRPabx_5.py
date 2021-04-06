
def sentence(words):
    for i, word in enumerate(words):
        article = ['a', 'an'][word[0] in 'aeiou']
        words[i] = '{} {}'.format(article, word)
    return '{} and {}.'.format(', '.join(words[:-1]), words[-1]).capitalize()

