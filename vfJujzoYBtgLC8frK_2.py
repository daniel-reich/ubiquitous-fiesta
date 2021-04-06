
import string
def word_to_decimal(word):
    lc = string.ascii_lowercase
    d = {x:lc.index(x) for x in word.lower()}
    base = 11 + max(d.values())
    return sum([(10 + d[x.lower()]) * base**i
         for i,  x in enumerate(word[::-1])])

