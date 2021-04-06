
def find_longest(s, long=0, ans=""):
    if type(s) == str:
        sent = ""
        for c in s.lower():
            sent += (c if c.isalpha() else ' ')
        s = sent.split()
        long = len(s[0])
        return find_longest(s[1:], long, s[0])
    if len(s) == 0:
        return ans
    if len(s[0]) > long:
        long = len(s[0])
        ans = s[0]
    return find_longest(s[1:], long, ans)

