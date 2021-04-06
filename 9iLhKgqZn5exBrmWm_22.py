
def ascending(txt):
  def consecutive(l,n):
    for u in range (l+1,len(txt)+1):
      if int(txt[l:u])==n+1:
        if u==len(txt):
          return True
        return consecutive(u,n+1)
    return False
  return any(consecutive(i,int(txt[:i])) for i in range (1,1+len(txt)//2))

