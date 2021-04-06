
def get_quartiles(lst, method):
  lst.sort()
  q0, q4 = min(lst), max(lst)
  if len(lst) % 2 == 0: q2 = sum(lst[len(lst)//2-1: len(lst)//2+1])/2
  else: q2 = lst[len(lst)//2]
  if method == "T":
    if len(lst) % 2 == 0: lst1, lst2 = lst[:len(lst)//2], lst[len(lst)//2:]
    else: lst1, lst2 = lst[:len(lst)//2+1], lst[len(lst)//2:]
    if len(lst1) % 2 == 0: q1 = sum(lst1[len(lst1)//2-1: len(lst1)//2+1])/2
    else: q1 = lst1[len(lst1)//2]
    if len(lst2) % 2 == 0: q3 = sum(lst2[len(lst2)//2-1: len(lst2)//2+1])/2
    else: q3 = lst2[len(lst2)//2]
  elif method == "MM":
    if len(lst) % 2 == 0: lst1, lst2 = lst[:len(lst)//2], lst[len(lst)//2:]
    else: lst1, lst2 = lst[:len(lst)//2], lst[len(lst)//2+1:]
    if len(lst1) % 2 == 0: q1 = sum(lst1[len(lst1)//2-1: len(lst1)//2+1])/2
    else: q1 = lst1[len(lst1)//2]
    if len(lst2) % 2 == 0: q3 = sum(lst2[len(lst2)//2-1: len(lst2)//2+1])/2
    else: q3 = lst2[len(lst2)//2]
  else:
    q1 = (len(lst)+1) / 4-1
    if q1 % 1 >= 0.5: q1 = int(q1//1 + 1)
    else: q1 = int(q1//1)
    q3 = (len(lst)+1) / 4 * 3-1
    if q3 % 1 <= 0.5: q3 = int(q3//1 )
    else: q3 = int(q3//1 +1)
    q1,q3 = lst[q1], lst[q3]
  return [q0,q1,q2,q3,q4]

