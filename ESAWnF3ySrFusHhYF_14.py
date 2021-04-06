
def edit_words(lst):
  for i in range(len(lst)):
    s,ls = lst[i].upper(),len(lst[i])//2
    s = s[:ls]+'-'+s[ls:]
    lst[i] = s[::-1]
  return lst

