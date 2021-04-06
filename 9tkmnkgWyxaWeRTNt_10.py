
def median(lst):
  slst = sorted(lst)
  if len(lst)%2 == 1:
    return slst[len(lst)//2]
  else:
    return (slst[len(lst)//2 - 1] + slst[len(lst)//2])/2

