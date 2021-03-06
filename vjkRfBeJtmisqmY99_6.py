
from itertools import permutations
​
def fit_words(words, clue):
    overlaps = ((0, -1, 3, -1), (0, 0, 4, -1), (0, 2, 2, 4), (1, -1, 5, 0), 
                (1, 0, 2, 0), (1, 4, 3, 2), (2, -1, 5, -1), (2, 0, 1, 0), 
                (2, 2, 4, 4), (2, 4, 0, 2), (3, -1, 0, -1), (3, 0, 4, 0), 
                (3, 2, 1, 4), (3, 4, 5, 2), (4, -1, 0, 0), (4, 0, 3, 0), 
                (4, 4, 2, 2), (5, -1, 2, -1), (5, 0, 1, -1), (5, 2, 3, 4))
    
    for w in permutations(words, 6):
        if all(w[a][b] == w[c][d] for a, b, c, d in overlaps) and w[2][3] == clue[-1]:
            return list(w)

