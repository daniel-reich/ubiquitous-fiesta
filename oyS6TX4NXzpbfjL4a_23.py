
def best_start(lst, word):
    letter_scores = {'a': 1,'b': 3,'c': 3,'d': 2,'e': 1,'f': 4,'g': 2,
                     'h': 4,'i': 1,'j': 8,'k': 5,'l': 2,'m': 3,'n': 1,
                     'o': 1,'p': 3,'q': 10,'r': 1,'s': 1,'t': 1,'u': 1,
                     'v': 4,'w': 4,'x': 8,'y': 4,'z': 10}
​
    wl = len(word)
    scores = []
    for sp in range(len(lst) - wl):
        score, wm = 0, 1
        for i in range(wl):
            bonus = lst[sp + i]
            score += letter_scores[word[i]] * (2 if bonus == "DL" else 3 if  bonus == 'TL' else 1)
            wm *= 2 if bonus == 'DW' else 1
        scores.append((score * wm, -sp))
    return -max(scores)[1]

