
def sort_by_string(lst, txt):
  sorts = list(txt)
  letters = []
  for word in lst:
    letters.append(word[0])
  for char in sorts:
    if char not in letters:
      sorts.remove(char)
  newlst = []
  for char in sorts:
    for word in lst:
      if word[0] == char:
        newlst.append(word)
  return newlst

