
def num_then_char(lst):
  n = sorted(j for i in lst for j in i if type(j) in (float,int))
  s = sorted(j for i in lst for j in i if type(j) == str)
  ns = n+s
  cur = 0
  for i in lst:
    for j in range(len(i)):
      i[j] = ns[cur]
      cur+=1
  return lst

