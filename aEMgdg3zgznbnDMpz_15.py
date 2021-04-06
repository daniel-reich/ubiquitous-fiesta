
def rotated_words(txt):
  return len(set([i for i in txt.split() if all([j in 'HIMNOSWXZ' for j in i])]))

