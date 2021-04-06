
def make_word_riddle(s):
  spl = s.lower().split('in')
  return (spl[-1][0]+spl[0][:]+spl[-1][1:]).upper()

