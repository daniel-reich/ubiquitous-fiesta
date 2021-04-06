
def same_line(lst):
  [a,b],[c,d],[e,f] = lst
  return not (a-c)*(b-f) - (b-d)*(a-e)

