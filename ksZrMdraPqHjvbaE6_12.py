
def largest_even(l):
  def find(l):
    if len(l)==1:return l[0]
    r=find(l[1:]) 
    return r if not r%2 or (r>l[0] and not r%2) else l[0]
  r=find(l)
  return r if not r%2 else -1

