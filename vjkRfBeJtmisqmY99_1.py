
import itertools
​
def fit_words(words, clue):
    clue_no, clue_letter = clue    
    for perm in itertools.permutations(words):
        w1, w2, w3, w4, w5, w6, w7, w8, w9 = perm
        if perm[clue_no - 1][3] != clue_letter:
            continue
        if w1[0] == w5[-1] and w1[2] == w3[4] and w1[-1] == w4[-1] and \
           w2[0] == w3[0] and w2[4] == w4[2] and w2[-1] == w6[0] and \
           w3[2] == w5[4] and w3[-1] == w6[-1] and \
           w4[0] == w5[0] and w4[4] == w6[2]:
            return [w1, w2, w3, w4, w5, w6]

