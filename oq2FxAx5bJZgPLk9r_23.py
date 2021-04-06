
def sock_merchant(lst):
  colors = set(lst)
  return sum([lst.count(i)//2 for i in colors])

