
def jumping_frog(n, s):
  def tree(c=1,i=0,h=[]):
    if i>=n: return c
    if i<0 or i in h or s[i]==0: return 99
    return min(tree(c+1,i+s[i],h+[i]),tree(c+1,i-s[i],h+[i]))
  a=tree()
  return a if a<99 else 'no chance :-('

