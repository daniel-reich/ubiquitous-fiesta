
def make_word_riddle(s):
  s = s.upper()
  i = s.find("IN")
  return s[i+2] + s[:i] + s[i+3:]

