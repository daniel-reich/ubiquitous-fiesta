
def conjugate(verb, pronoun):
    suf = {1: ['Io', 'o'], 2: ['Tu', 'i'], 3: ['Egli', 'a'],
           4: ['Noi', 'iamo'], 5: ['Voi', 'ate'], 6: ['Essi', 'ano']}
    if verb[:-3].endswith('i') and pronoun == 2:
        return suf[pronoun][0] + ' ' + verb[:-3]
    if verb[:-3].endswith('i') and pronoun == 4:
        return suf[pronoun][0] + ' ' + verb[:-3] + suf[pronoun][1][1:]
    if verb[:-3].endswith('c') and pronoun == 2:
        return suf[pronoun][0] + ' ' + verb[:-3] + 'h' + suf[pronoun][1]
    if verb[:-3].endswith('c') and pronoun == 4:
        return suf[pronoun][0] + ' ' + verb[:-3] + 'h' + suf[pronoun][1]
    if verb[:-3].endswith('g') and pronoun == 2:
        return suf[pronoun][0] + ' ' + verb[:-3] + 'h' + suf[pronoun][1]
    if verb[:-3].endswith('g') and pronoun == 4:
        return suf[pronoun][0] + ' ' + verb[:-3] + 'h' + suf[pronoun][1]
    else:
        return suf[pronoun][0] + ' ' + verb[:-3] + suf[pronoun][1]

