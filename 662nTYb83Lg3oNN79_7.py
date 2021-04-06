
def is_parallelogram(lst):
  lst.sort()
  return (lst[0][1]-lst[1][1])*(lst[3][0]-lst[2][0])==(lst[0][0]-lst[1][0])*(lst[3][1]-lst[2][1])

