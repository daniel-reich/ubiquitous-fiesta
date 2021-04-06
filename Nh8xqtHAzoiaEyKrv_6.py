
def correct_sentences(s):
  x = " ".join(i for i in s.split())
  for i in x:
    if i.isupper():
      i = x.index(i)
      x = x[:i-1] + "." + x[i-1:]
  return x[0].capitalize() + x[1:] + "."

