
def constraint(txt):
    s1 = set( chr(Z) for Z in range(ord('a'), ord('z')))
    if all(Z in txt.lower() for Z in s1):
        return "Pangram"
    if all(txt.count(Z) < 2 for Z in s1):
        return "Heterogram"
    if all(txt.lower().split()[0][0] == Z[0] for Z in txt.lower().split()):
        return "Tautogram"
    for W in txt.lower().split()[0]:
        if all(W in Z for Z in txt.lower().split()):
            return "Transgram"
    return "Sentence"

