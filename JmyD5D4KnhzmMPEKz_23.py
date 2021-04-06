
import string
def constraint(txt):
    x = string.ascii_lowercase
    txt = txt.lower()
    if is_pangram(txt, x):      return 'Pangram'
    if is_heterogram(txt):      return 'Heterogram'
    if is_tautogram(txt):       return 'Tautogram'
    if is_transgram(txt):       return 'Transgram'
    return 'Sentence'
​
def is_pangram(txt, x):
    for ch in x:
        if ch not in txt:
            return False
    return True
​
def is_heterogram(txt):
    for ch in txt:
        if ch.isalpha() and txt.count(ch) != 1:
            return False
    return True
​
def is_tautogram(txt):
    return len(set([x[0] for x in txt.split()])) == 1
​
def is_transgram(txt):
    los = [set(x) for x in txt.split()]
    return len(set.intersection(*los)) > 0

