
def fit_words(words, clue):
    sols3 = [[w] for w in words if w[3] == clue[1]]
    sols13 = [[w]+s for w in words for s in sols3
              if w[2] == s[0][4] and w not in s]
    sols123 = [[s[0], w, s[1]] for w in words for s in sols13
               if w[0] == s[1][0] and w not in s]
    sols1234 = [s + [w] for w in words for s in sols123
                if w[-1] == s[0][-1] and w[2] == s[1][4] and w not in s]
    sols12345 = [s + [w] for w in words for s in sols1234
                 if w[0] == s[3][0] and w[2] == s[1][2] and
                 w[4] == s[2][2] and w not in s]
    sols = [s + [w] for w in words for s in sols12345
            if w[0] == s[1][-1] and w[2] == s[3][4] and
            w[4] == s[0][4] and w[-1] == s[2][-1] and w not in s]
​
    return sols[0]

