
def numbers_need_friends_too(n):
  n=str(n)
  ans=''
  if n[0]!=n[1]:ans+=n[0]*3
  else:ans+=n[0]
  if len(n)>2:
    for i in range(1,len(n)-1):
      if n[i]==n[i-1] or n[i]==n[i+1]:ans+=n[i]
      else:ans+=n[i]*3
  if n[-1]!=n[-2]:ans+=n[-1]*3
  else:ans+=n[-1]
  return int(ans)

