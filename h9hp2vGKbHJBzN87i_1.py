
def partially_hide(phrase):
    return ' '.join([word[0] + '-' * (len(word)-2) + word[-1] for word in phrase.split()])

