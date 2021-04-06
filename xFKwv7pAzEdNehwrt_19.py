
def bracket_logic(s):
    s = ''.join(i for i in s if i in "()[]{}<>")
    while any(pair in s for pair in ('()', '[]', '{}', '<>')):
        for pair in ('()', '[]', '{}', '<>'):
            s = s.replace(pair, '')
    return not s

