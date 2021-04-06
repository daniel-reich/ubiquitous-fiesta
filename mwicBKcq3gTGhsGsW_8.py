
def make_word_riddle(s):
  s = s.lower()
  i_index = s.find('in')
  word = s[i_index + 2:].upper()
  letters = s[:i_index].upper()
  return word[0] + letters + word[1:]

