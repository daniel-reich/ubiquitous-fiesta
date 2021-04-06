
def find_shortest_words(txt):
  words = txt[:-1].lower().split()
  tlst = []
  for word in words:
    if not word.isalpha():
      continue
    tlst.append((len(word), word))
  tlst.sort()
  wds = []
  for l, w in tlst:
    if l == tlst[0][0]:
      wds.append(w)
  return wds

