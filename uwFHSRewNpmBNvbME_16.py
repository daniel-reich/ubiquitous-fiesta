
def same_vowel_group(w):
    vow = set('aeiou')
    ls = [set(words).intersection(vow) for words in w]
    lo =  [w[i] for i in range(len(w)) if ls.count(ls[i]) > 1]
    return lo if len(lo)>0 else [w[0]]

