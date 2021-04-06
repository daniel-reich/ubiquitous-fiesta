
def gcf(n1, n2): 
  cf_list = []
  if n2 > n1:
    for f in range(1, n1+1):
      if n1 % f == 0 and n2 % f == 0:
        cf_list.append(f)
    return max(cf_list)
  else:
    for f in range(1, n2+1):
      if n1 % f == 0 and n2 % f == 0:
        cf_list.append(f)
    return max(cf_list)
​
def simplify(txt):
  list_nums = txt.split('/')
  N = int(list_nums[0])
  D = int(list_nums[1])
  if (N/D) % 1 == 0:
    return str(int(N/D))
  else:
    top = str(int(N/gcf(N,D)))
    bottom = str(int(D/gcf(N,D)))
    return top + '/' + bottom

