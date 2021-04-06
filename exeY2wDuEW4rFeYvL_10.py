
def ordered_matrix(a, b):
  lst = list(range(1, a*b + 1))
  return [lst[i:i+b] for i in range(0,len(lst),b)]

