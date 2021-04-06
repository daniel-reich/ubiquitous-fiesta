
def count(n):
  lst2 = []
  for i in str(n):
    if i != '-':
      lst2.append(i)
  return len(lst2)

