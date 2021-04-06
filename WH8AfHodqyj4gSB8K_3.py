
def is_authentic_skewer(s):
    if not (s[0].isalpha() and s[-1].isalpha() and len(s) > 4):
        return False
    dash_len, begin = [], 0
    for i, c in enumerate(s):
        if c.isalpha():
            if i > 0:
                dash_len.append(i - begin - 1)
                begin = i
    if len(set(dash_len)) > 1:
        return False
    return all(c in 'AEIOU' if i % 2 else c not in 'AEIOU'
               for i, c in enumerate(s.split('-' * dash_len[0])))

