
def make_word_riddle(s):
  l = s.lower().split("in")
  return (l[1][0] + l[0] + l[1][1:]).upper()

