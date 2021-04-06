
def seven_segment(txt):
    digits = {'0': 'abcdef ', '1': ' bc    ', '2': 'ab de g', 
              '3': 'abcd  g', '4': ' bc  fg', '5': 'a cd fg', 
              '6': 'a cdefg', '7': 'abc    ', '8': 'abcdefg', 
              '9': 'abc  fg'}
    res = []
    for d1, d2 in zip(txt, txt[1:]):
        changes = []
        for s1, s2 in zip(digits[d1], digits[d2]):
            if s1 < s2:
                changes += s2.upper()
            elif s1 > s2:
                changes += s1
        res += [changes]
    return res

