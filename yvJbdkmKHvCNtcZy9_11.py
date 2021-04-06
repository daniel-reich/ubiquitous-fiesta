
def is_disarium(n):
  list1 = []
  a = 1
  total = 0
  for i in str(n):
    list1.append(int(i))
  for i in list1:
    total += i**a
    a+=1
  return total == int(n)

