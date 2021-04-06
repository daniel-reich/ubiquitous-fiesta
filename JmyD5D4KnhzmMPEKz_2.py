
def constraint(txt):
    if len([char for char in set(txt.lower()) if char.isalpha()]) == 26:
        return 'Pangram'
    if len(set(txt.lower().replace(' ', ''))) == len(txt.replace(' ', '')):
        return 'Heterogram'
    if len(set([word[0] for word in txt.lower().split()])) == 1:
        return 'Tautogram'
    same = [char for char in txt.lower().split()[0]]
    for word in txt.lower().split()[1:]:
        for char in same:
            if char not in word:
                same.remove(char)
    return 'Transgram' if same else 'Sentence'

