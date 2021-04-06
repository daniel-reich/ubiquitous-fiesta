
def make_word_riddle(s):
  first, last = s.upper().split('IN')
  return last[0] + first + last[1:]

