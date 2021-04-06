
def maximum_seating(lst):
  s=sum(lst)
  i=0
  while i<len(lst):
    if i<2:
      A=lst[:i+3]
    elif 2<=i<len(lst)-2:
      A=lst[i-2:i+3]
    else:
      A=lst[i-2:]
    if all(x==0 for x in A):
      lst[i]=1
    i+=1
  return sum(lst)-s

