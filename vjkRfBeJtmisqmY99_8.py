
cross = [[], [(1, 4, 0, 4)], [(2, 4, 0, 2), (2, 6, 1, 6)], [(3, 4, 1, 2),
        (3, 6, 0, 6)], [(4, 0, 3, 0), (4, 4, 2, 2), (4, 6, 0, 0)],
        [(5, 0, 2, 0), (5, 2, 4, 2), (5, 4, 3, 2), (5, 6, 1, 0)]]
​
def fit_words(words, clue):
    def check(lst):
        return all(res[w1][i1]==res[w2][i2] for w1, i1, w2, i2 in lst)
    
    def fitnext(level):
        if level>5: return res[clue[0]-1][3] == clue[1]
        for i, word in enumerate(words):
            if used[i]: continue
            res[level] = word
            used[i] = True
            if check(cross[level]) and fitnext(level+1):
                return True
            used[i] = False
            
    used = [False] * 9
    res = [None] * 6
    fitnext(0)
    res[1], res[5] = res[5], res[1]
    return res

