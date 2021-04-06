
def make_word_riddle(s):
    x = s.lower().index('in')
    return ''.join(s[x+2] + s[:x] + s[x+3:]).upper()

