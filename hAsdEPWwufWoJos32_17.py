
def no_yelling(phrase):
    while phrase.endswith('??'):
        phrase = phrase[:-2] + '?'
    while phrase.endswith('!!'):
        phrase = phrase[:-2] + '!'
    return phrase

