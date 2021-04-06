
def remove_letters(letters, word):
  lst = []
  for i in word:
    lst.append(i)
  for j in letters:
    if j in lst:
      letters.remove(j)
      lst.remove(j)
  for k in letters:
    if k in lst:
      letters.remove(k)
      lst.remove(k)
  for a in letters:
    if a in lst:
      letters.remove(a)
      lst.remove(a)
  return letters

