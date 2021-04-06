
def sentence(words):
    words = list(map(lambda x: 'an '+ x  if x[0] in 'aeiou' else 'a ' + x , words))
    l = ' and ' + words[-1] +'.'
    return ', '.join(words[:len(words)-1]).capitalize() + l

