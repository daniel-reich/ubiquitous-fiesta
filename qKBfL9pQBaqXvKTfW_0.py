
def sum_of_slices(lst):
  r=[0]
  for i in lst:
    if r[-1]+i<=100: r[-1]+=i
    else: r.append(i)
  return r

