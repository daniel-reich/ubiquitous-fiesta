
def base_conv(n, b):
  if type(n)==int:
    Note='abcdefghijklmnopqrstuvwxyz'
    q,r=divmod(n,b)
    N=Note[r]
    return base_conv(q, b)+N if q else N
  else:
    if all(ord(x)-ord('a')<b for x in n) and ' ' not in n:
      return sum((ord(n[i])-ord('a'))*(b**(len(n)-i-1)) for i in range(len(n)))
    else:
      return "{} is not a base {} number.".format(n,b)

