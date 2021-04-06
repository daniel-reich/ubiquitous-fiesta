
from re import findall
def haiku(st):
    res = [0, 0, 0]
    for i, s in enumerate(st.split('/')):
        for w in s.split():
            w = w.strip(',')
            count = len(findall(r'[aeiouyAEIOUY]{1,3}', w))
            if count > 1 and (w.endswith('e') or w.endswith('es')
                              or w.endswith('e\'s')):
                count -= 1
            res[i] += count
    return res == [5, 7, 5]

