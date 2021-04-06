
def make_word_riddle(s):
    s = s.upper()
    idx = s.find("IN")
    pre = s[:idx]
    post = s[idx+2:]
    return post[0] + pre + post[1:]

