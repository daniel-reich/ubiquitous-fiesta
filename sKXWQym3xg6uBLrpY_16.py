
def iqr(lst):
  lst.sort()
  if len(lst)%2 == 1:
    Q1,Q3 = lst[:len(lst)//2],lst[(len(lst)//2)+1:]
  else:
    Q1,Q3 = lst[:len(lst)//2],lst[len(lst)//2:]
  if len(Q1)%2 == 1:
    Q1 = Q1[len(Q1)//2]
  else:
    Q1 = (Q1[(len(Q1)//2)-1]+Q1[len(Q1)//2])/2
  if len(Q3)%2 == 1:
    Q3 = Q3[len(Q3)//2]
  else:
    Q3 = (Q3[(len(Q3)//2)-1]+Q3[len(Q3)//2])/2
  return Q3 - Q1

