
def difference_two(l):
  l = [[i,j] for i in l for j in l if abs(i-j)==2]
  ls = []
  for i in l: 
    if sorted(i) not in ls: ls.append(sorted(i))
  return sorted(ls)

