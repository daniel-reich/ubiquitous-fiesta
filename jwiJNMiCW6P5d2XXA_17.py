
def does_rhyme(txt1, txt2):
  w1, w2 = txt1.split()[-1].lower(), txt2.split()[-1].lower()
  f = lambda x: sorted([item for item in x if item in 'aeiou'])
  return f(w1)==f(w2)

