
def numbers_need_friends_too(n):
  t,s,l="",str(n),len(str(n))
  for i,x in enumerate(s):
    if (not i and s[i+1]!=x) or (i==l-1 and s[i-1]!=x) or (0<i<l-1 and x not in s[i-1:i+2:2]):
      t+=x*3
    else:
      t+=x
  return int(t)

