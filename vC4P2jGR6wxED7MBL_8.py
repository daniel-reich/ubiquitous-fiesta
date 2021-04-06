
def larger_than_right(lst):
  return [lst[x] for x in range(len(lst)) if all(lst[x]>lst[y] for y in range(x+1, len(lst)))]

