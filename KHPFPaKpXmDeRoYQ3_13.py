
def check_score(s):
    d = {'#':5, 'O':3, 'X':1,
         '!':-1, '!!':-3, '!!!':-5}
    tot = 0
    for i in range(len(s)):
        for j in range(len(s[i])):
            tot += d[s[i][j]]
    if tot < 0:
        return 0
    return tot

