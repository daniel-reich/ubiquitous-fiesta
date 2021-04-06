
def same_letter_pattern(txt1, txt2):
  pattern = lambda x: [x.index(i) for i in x]
  return pattern(txt1) == pattern(txt2)

