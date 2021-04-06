
def replace(txt, r):
  word = []
  for a in range(len(txt)):
    if ord(txt[a]) in range(ord(r[0]), ord(r[2])+1):
      word.append("#")
    else:
      word.append(txt[a])
  return "".join(word)

