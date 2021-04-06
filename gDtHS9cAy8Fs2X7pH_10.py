
def count_repetitions(lst):
  dict = {}
  for i in range(0, len(lst)):
    rep = 0
    for j in range(0, len(lst)):
      if (lst[i] == lst[j]):
        rep += 1 
    dict[lst[i]] = rep
  return dict

