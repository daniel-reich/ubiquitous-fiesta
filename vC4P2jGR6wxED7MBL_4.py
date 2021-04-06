
def larger_than_right(lst):
  return [lst[i] for i in range(len(lst)) if all(lst[i]>lst[k] for k in range(i+1,len(lst)))]

