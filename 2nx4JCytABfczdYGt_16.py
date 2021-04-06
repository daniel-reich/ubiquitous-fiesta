
def conjugate(verb, pronoun):
    d = {1:['Io', 'o'],
         2:['Tu', 'i'],
         3:['Egli', 'a'],
         4:['Noi', 'iamo'],
         5:['Voi', 'ate'],
         6:['Essi', 'ano']}
    root = verb[:-3]
    pro, suff = d[pronoun]
    if root[-1] in ('c', 'g') and pronoun in (2, 4):
        root = root + 'h'
    if root[-1] == 'i' and pronoun in (2, 4):
        suff = suff[1:]
    return pro + ' ' + root + suff

