
def quad_sequence(lst):
  x=len(lst)
  for n in range(x-1,2*x-1):
    p=lst[-1]
    lst.append(p+(lst[1]-lst[0])+(lst[0]-2*lst[1]+lst[2])*n)
  return lst [x:]

