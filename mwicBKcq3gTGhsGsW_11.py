
def make_word_riddle(s):
  r = s.upper().index("IN")
  return (s[r+2] + s[:r] + s[r+3:]).upper()

