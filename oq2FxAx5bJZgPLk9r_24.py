
def sock_merchant(lst):
  p=0
  for x in set(lst):
    d,r=divmod(lst.count(x),2)
    p+=d
  return p

