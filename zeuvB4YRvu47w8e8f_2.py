
def full_cycle(lst):
  travel = lambda lst, i: lst[i] if i < len(lst) else False
  used = []
  c = 0
  i = 0
  print(lst)
  while len(set(used)) == len(used) < len(lst) and c < 1000:
    used.append(i)
    i = travel(lst, i)
    print(i, used)
    if i == False:
      return len(set(used)) == len(lst) if max(used) < len(lst) else False
    c += 1
  
  return len(set(used)) == len(lst)

