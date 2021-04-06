
def balanced(lst):
  l,r = lst[:len(lst)//2],lst[len(lst)//2:]
  return l*2 if sum(l)>sum(r) else r*2 if sum(l)<sum(r) else lst

