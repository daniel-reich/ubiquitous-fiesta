
def sort_by_string(lst, txt):
  first_l_lst = [word[0] for word in lst]
  for x in txt:
    if x not in first_l_lst:
      txt = txt.replace(x, "")
  #myDict = [x for x in enumerate(txt)]
  return [j for a in txt for j in lst if j.startswith(a)]

