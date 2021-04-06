
def missing_letter(lst):
  a=len(lst)
  b=ord(lst[0])
  for i in range(1,a):
    c=ord(lst[i])
    if(c-b!=1):
      d=b+1
      return chr(d)
    else:
      b=c

