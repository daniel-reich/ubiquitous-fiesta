
def trans(lst):
    return list(zip(*lst))[::-1]
def spiral_order(matrix):
  lst1=[]
  while matrix:
    lst1+=matrix.pop(0)
    matrix=trans(matrix)
  return lst1

