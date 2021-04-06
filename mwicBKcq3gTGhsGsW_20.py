
def make_word_riddle(s):
  start,mid,end = s.lower().partition('in')
  new_word = end[0:1]+start+end[1:]
  return new_word.upper()

