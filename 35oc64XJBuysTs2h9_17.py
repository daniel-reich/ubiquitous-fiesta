
def get_quartiles(lst, method):
  lst = sorted(lst)
  if method == "T" or method == "MM":
    if len(lst)%2 == 0:
      pq2 = int(len(lst)/2)
      q2 = (lst[pq2] + lst[pq2-1])/2
      lst1 ,lst2 = lst[:pq2], lst[pq2:]
    else:
      pq2 = int(len(lst)/2)
      q2 = lst[pq2]
      if method == "T" :
        lst1 ,lst2 = lst[:pq2+1], lst[pq2:]
      else:
        lst1 ,lst2 = lst[:pq2], lst[pq2+1:]
    print(lst1,lst2, pq2)
    if len(lst1)%2 == 0:
      pq1 = int(len(lst1)/2)
      q1 = (lst1[pq1] + lst1[pq1-1])/2
    else:
      pq1 = int(len(lst1)/2)
      q1 = lst1[pq1]
​
    if len(lst2)%2 == 0:
      pq3 = int(len(lst2)/2)
      q3 = (lst2[pq3] + lst2[pq3-1])/2
    else:
      pq3 = int(len(lst2)/2)
      q3 = lst2[pq3]
  else:
    if len(lst)%2 == 0:
      pq2 = int(len(lst)/2)
      q2 = (lst[pq2] + lst[pq2-1])/2
    else:
      pq2 = int(len(lst)/2)
      q2 = lst[pq2]
    print (lst, round(2.5))
    q1 = lst[round((len(lst)+1)/4+0.00000000001)-1]
    q3 = lst[round((3*len(lst)+3)/4-0.00000000001)-1]
​
​
  return [lst[0], q1, q2, q3, lst[-1]]
​
print(get_quartiles([2, 6, 1, 8, 5, 9, 7, 4, 3], "MS"))

