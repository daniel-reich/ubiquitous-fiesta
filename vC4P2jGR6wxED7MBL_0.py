
def larger_than_right(lst): 
  return [i for idx, i in enumerate(lst) if all(i > j for j in lst[idx+1:])]

