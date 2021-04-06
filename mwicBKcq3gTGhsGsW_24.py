
def make_word_riddle(s):
  a = s.upper().split("IN")[0]
  b = s.upper().split("IN")[1]
  return (b[:1] + a + b[1:])

