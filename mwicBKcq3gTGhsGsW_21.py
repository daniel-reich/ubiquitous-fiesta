
def make_word_riddle(s):
  return s.upper().split("IN")[-1][0] + s.upper().split("IN")[0] + s.upper().split("IN")[-1][1:]

