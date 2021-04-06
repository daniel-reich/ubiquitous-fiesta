
def sort_by_string(lst, txt):
  final = []
  fa = final.append
  for c in txt:
    selected = list(filter(lambda w:w[0]==c, lst))
    if len(selected)>0:
      fa(selected[0])
  return final

