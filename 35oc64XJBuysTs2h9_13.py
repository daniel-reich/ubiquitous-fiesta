
from statistics import median
def get_quartiles(lst, method):
  lst.sort()
  q0,q4 = lst[0],lst[-1]
  q2 = median(lst)
  if method == "MS":
    k1 = round((len(lst) + 1) / 4)
    k2 = round((3 * (len(lst) + 1)) / 4)
    if (len(lst) + 1) % 4 == 2:
      k1 += 1
      k2 -= 1
    q1,q3 = lst[round(k1)-1],lst[round(k2)-1]
  else:
    if len(lst) % 2 == 0:
      lst1,lst2 = lst[:len(lst)//2],lst[len(lst)//2::]
    else:
      lst1,lst2 = lst[:len(lst)//2],lst[len(lst)//2 + 1::]
      if method == "T":
        lst1.append(q2)
        lst2.insert(0,q2)
    q1,q3 = median(lst1),median(lst2)
  return [q0,q1,q2,q3,q4]

