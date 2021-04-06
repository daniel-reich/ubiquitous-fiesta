
def conjugate(verb, pronoun):
    rel = (0,
           ('Io', 'o'),
           ('Tu', 'i'),
           ('Egli', 'a'),
           ('Noi', 'iamo'),
           ('Voi', 'ate'),
           ('Essi', 'ano')
           )
    if verb[-4] == 'i' and pronoun in (2,4):
        word = verb[:-4] + verb[-3:]
    elif verb[-4] in 'cg':
        word = verb[:-3] + 'h' + verb[-3:]
    else:
        word = verb
    return '{} {}'.format(rel[pronoun][0], 
  word.replace(verb[-3:], rel[pronoun][1]))

