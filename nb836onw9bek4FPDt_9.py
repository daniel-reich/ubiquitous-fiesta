
def count_same_ends(txt):
  for i in txt:
    if i.isalpha()==False and i.isspace()==False:
      txt=(txt.replace(i,"")).lower()
  return sum([1 for i in txt.split() if i[0]==i[-1] and len(i)>1])

