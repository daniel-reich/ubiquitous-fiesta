
def make_word_riddle(s):
  return (s.lower().split('in')[1][0] + s.lower().split('in')[0] + s.lower().split('in')[1][1:]).upper()

