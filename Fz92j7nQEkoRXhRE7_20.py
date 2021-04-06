
def jumping_frog(n, s):
  h,t = 0,0
  while True:
    h+=s[h]
    t+=1
    if h >= len(s): break
    if s[h]==0:return "no chance :-("
    if h>0 and s[h-1]>s[h] and h+s[h-1]>len(s):
      h-=1
      t+=1
      continue
  return t+1

