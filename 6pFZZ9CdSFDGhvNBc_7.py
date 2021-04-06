
def factor_group(num):
  lst = []
  for i in range(1,num+1):
    if num%i == 0:
      lst.append(i)
  if len(lst)%2 == 0:
    return "even"
  else:
    return "odd"

