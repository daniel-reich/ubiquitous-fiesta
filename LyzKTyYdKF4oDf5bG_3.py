
def find_longest(s, res=None):
    if res is None:
        s = (s.lower().replace(',', '').replace('.', '').replace('\'s', '')
             .replace('\"', '').split())
        res, s = s[0], s[1:]
    return (find_longest(s[1:], s[0]) if len(s[0]) > len(res)
            else find_longest(s[1:], res)) if s else res

