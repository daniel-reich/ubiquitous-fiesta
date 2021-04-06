
def sort_by_letter(lst):
  letters = []
  for i in lst:
    for j in i:
      if j.isalpha():
        letters.append(j)
  letters.sort()
  newlst = []
  for i in letters:
    for j in lst:
      if i in j:
        newlst.append(j)
  return newlst

