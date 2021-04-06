
def syllabification(word):
    v = 'aAeiou'
    lst_idx_v = [i for i, l in enumerate(word) if l in v]
    if len(lst_idx_v) == 1:
        return word
    begin = 0
    syllables = []
    for i in range(1, len(lst_idx_v)):
        syllables.append(word[begin: lst_idx_v[i] - 1])
        begin = lst_idx_v[i] - 1
    syllables.append(word[begin:])
    return '.'.join(syllables)

