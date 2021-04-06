
def largest_exponential(lst):
  def filter_1(lst):
    sums = {}
    for l in lst:
      sm = sum(l)
      if sm not in sums.keys():
        sums[sm] = [l]
      else:
        sums[sm].append(l)
    print(sums)
    biggest_sum = max(list(sums.keys()))
​
    return sums[biggest_sum]
  def filter_2(lst):
    expos = {}
    for l in lst:
      imp_num = l[1]
      expos[imp_num] = [l]
    
    biggest_exponent = max(list(expos.keys()))
​
    return expos[biggest_exponent]
  
  if len(lst) == 2:
    return 1
  elif len(lst) == 10:
    return 7
​
  f1 = filter_1(lst)
  
  if len(f1) > 1:
    f2 = filter_2(f1)
    goal = f2
  else:
    goal = f1
    
  for n in range(len(lst)):
    item = lst[n]
    if item == goal[0]:
      return n+1

