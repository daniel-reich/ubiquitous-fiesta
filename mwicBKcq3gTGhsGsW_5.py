
def make_word_riddle(s):
    idx = s.lower().index('in')
    return s[idx+2].upper()+s[:idx].upper()+s[idx+3:].upper()

