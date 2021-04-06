
def sort_by_last(txt):
  chars = [w[-1] for w in txt.split()]
  s = []
  words = txt.split()
  for c in sorted(list(set(chars))):
    for word in words:
      if word[-1]==c:
        s.append(word)
  return " ".join(s)

