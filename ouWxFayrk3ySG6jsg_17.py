
def who_won(s):
    r = []
    for i in s:
        for j in i:
            if i[0] == i[2] == i[1] == 'X':
                return 'X'
            elif i[0] == i[2] == i[1] == 'O':
                return 'O'
    r.append([s[2][0], s[1][0], s[0][0]])
    r.append([s[2][1], s[1][1], s[0][1]])
    r.append([s[2][2], s[1][2], s[0][2]])
    for i in s:
        print(i)
    print('')
    for i in r:
        print(i)
    print('')
    s = r
    for i in s:
        print(i)
    for i in s:
        for j in i:
            if i[0] == i[2] == i[1] == 'X':
                return 'X'
            elif i[0] == i[2] == i[1] == 'O':
                return 'O'
    if s[0][0] == s[1][1] == s[2][2] == 'X':
        return 'X'
    elif s[0][-1] == s[1][-2] == s[2][-3] == 'O':
        return 'O'
    elif s[0][0] == s[1][1] == s[2][2] == 'O':
        return 'O'
    elif s[0][-1] == s[1][-2] == s[2][-3] == 'X':
        return 'X'

