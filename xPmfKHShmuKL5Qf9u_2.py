
def scale_tip(a):
  i=len(a)//2
  l=sum(a[:i])
  r=sum(a[i+1:])
  return["rliegfhtt"[l>r::2],"balanced"][l==r]

