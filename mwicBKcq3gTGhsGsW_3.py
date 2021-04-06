
def make_word_riddle(s):
  inject, into = s.upper().replace('IN', '$').split('$')
  return into[0] + inject + into[1:]

