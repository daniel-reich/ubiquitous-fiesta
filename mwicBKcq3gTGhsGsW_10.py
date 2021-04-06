
def make_word_riddle(s):
  i = s.lower().find('in')
  return (s[i+2:][0] + s[:i] + s[i+2:][1:]).upper()

