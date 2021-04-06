
def is_checkerboard(lst):
  ul = lst[0][0]
  even = [int(i%2 != ul) for i in range(len(lst))]
  odd = [int(i%2 == ul) for i in range(len(lst))] 
  return all([row == [even, odd][i%2] for i,row in enumerate(lst)])

