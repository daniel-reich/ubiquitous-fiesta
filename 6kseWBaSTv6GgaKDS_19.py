
def next_letters(s):
    if s == '': return 'A'
    ALPHA_DICT = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
                  'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    s = list(s)
    for i in range(len(s) - 1, -1, -1):
        if ALPHA_DICT[s[i]] == 25:
            s[i] = 'A'
            if i == 0:
                s.insert(0, 'A')
        else:
            value = ALPHA_DICT[s[i]] + 1
            value = list(ALPHA_DICT.keys())[list(ALPHA_DICT.values()).index(value)]
            s[i] = value
            break
    return ''.join(s)

