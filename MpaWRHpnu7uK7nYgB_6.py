
def doubleton(n):
  s = n + 1
  while len(set(list(str(s))))!=2:
    s+=1
  return s

