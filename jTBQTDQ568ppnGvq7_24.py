
def digit_sort(lst):
  s=[sorted([i for i in filter(lambda x:len(str(x))==j,lst)]) for j in range(len(str(max(lst))),0,-1)]
  return [h for i in s for h in i]

