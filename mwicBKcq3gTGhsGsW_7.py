
def make_word_riddle(s):
  try:
    return (s[s.index("in")+2] + s[:s.index("in")] + s[s.index("in")+3:]).upper()
  except:
    return (s[s.index("IN")+2] + s[:s.index("IN")] + s[s.index("IN")+3:]).upper()

