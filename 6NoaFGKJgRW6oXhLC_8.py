
from collections import Counter
def sum_of_vowels(sentence):
    vowels = {'a': 4, 'e': 3, 'i': 1}
    x = dict(Counter([v.lower() for v in sentence if v.lower() in vowels]))
    return sum([vowels[key] * x[key] for key in x.keys()])

