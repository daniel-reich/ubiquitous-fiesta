
def best_start(lst, word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    vals = (1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 2, 3, 
            1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10)
    d = dict(zip(letters, vals))
​
    res = []
    for i in range(len(lst) - len(word) + 1):
        score, group = 0, zip(word, lst[i:])
        for letter, mult in group:
            if mult == 'DL':
                score += d[letter] * 2
            elif mult == 'TL':
                score += d[letter] * 3
            else:
                score += d[letter]
        if 'DW' in lst[i:i+len(word)]:
            score *= 2
        res.append((i, score))
    
    return max(res, key=lambda x: x[1])[0]

