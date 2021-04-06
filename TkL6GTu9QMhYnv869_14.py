
def add_ending(lst, ending):
  a = []
  for i in range(len(lst)):
    a1 = []
    a1.append(lst[i])
    a1.append(ending)
    a.append(''.join(a1))
  return a

