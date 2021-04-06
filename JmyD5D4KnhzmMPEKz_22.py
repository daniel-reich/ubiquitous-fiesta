
from string import ascii_lowercase
from collections import Counter
​
def constraint(txt):
    txt = txt.lower()
​
    def pangram(txt):
        result = set(
            i for i in txt if i.isalpha()
        ) == set(ascii_lowercase)
        return 'Pangram' if result else (heterogram(txt))
​
    def heterogram(txt):
        c = Counter(i for i in txt if i.isalpha())
        d = Counter(ascii_lowercase)
        result = not c - d
        return 'Heterogram' if result else (tautogram(txt))
​
    def tautogram(txt):
        result = len(set(i[0] for i in txt.split())) == 1
        return 'Tautogram' if result else (transgram(txt))
​
    def transgram(txt):
        first, *rest = (
            tuple(i) for i in txt.split() if i.isalpha())
        result = set(first).intersection(*rest)
        return 'Transgram' if result else 'Sentence'
​
    return pangram(txt)

