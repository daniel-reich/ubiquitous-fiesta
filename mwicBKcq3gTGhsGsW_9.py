
def make_word_riddle(s):
    s = s.upper()
    ind = s.index("IN")
    a = s[: ind]
    b = list(s[ind + 2 :])
    b.insert(1, a)
    return "".join(b)

