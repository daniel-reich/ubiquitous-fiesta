
def correct_sentences(s):
  i = 0
  st = s.split()
  while i < len(st):
    if st[i].islower()==False:
      st[i-1] = st[i-1] + "."
    i =i + 1
  st[i-1] = st[i-1]+"."
  st[0] = str(st[0]).capitalize()
  sentence = " ".join(map(str, st))
  return sentence

