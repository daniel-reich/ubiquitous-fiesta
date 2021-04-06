
from re import findall
def ing_extractor(s):
    return [w for w in findall(r'\b([\w*]+ing|[\w*]+ING)\b', s)
            if sum(c in 'aeiouAEIOU0*' for c in w) > 1]

