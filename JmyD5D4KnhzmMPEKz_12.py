
def constraint(txt):
    letters = [i.lower() for i in txt if i.lower().isalpha()]
    words = txt.split()
    if len(set(letters)) == 26:
        return 'Pangram'
    if len(set(letters)) == len(letters):
        return 'Heterogram'
    if len({i.lower()[0] for i in words}) == 1:
        return 'Tautogram'
    s = set(words[0].lower())
    for i in range(1, len(words)):
        s.intersection_update(words[i].lower())
    if len(s) > 0 or len(words) == 1:
        return 'Transgram'
    return 'Sentence'

