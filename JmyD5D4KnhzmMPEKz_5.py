
def constraint(txt):
    clean = ''.join(i for i in txt.lower() if i.isalpha() or i.isspace())
    words = clean.split()
    strng = clean.replace(' ', '')
​
    if len(set(strng)) == 26:
        return 'Pangram'
    if len(set(strng)) == len(strng):
        return 'Heterogram'
    if len({i[0] for i in words}) == 1:
        return 'Tautogram'
    for i in words[0]:
        if all(i in w for w in words):
            return 'Transgram'
    return 'Sentence'

