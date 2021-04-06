
def rotated_words(txt):
  return len(set([i for i in txt.split() if set(i).issubset('HINOSXZWM')]))

