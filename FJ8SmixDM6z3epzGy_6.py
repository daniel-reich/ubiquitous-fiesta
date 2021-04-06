
def check_perfect(num):
  xlist = []
  for i in range(1,num):
    if num % i == 0:
      xlist.append(i)
  if sum(xlist) == num:
    return True
  else:
    return False

