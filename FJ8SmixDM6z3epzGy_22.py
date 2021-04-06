
def check_perfect(num):
  lst = []
  a=1
  while a < num:
    if num % a == 0:
      lst.append(a)
    a+=1
  if sum(lst) == num:
    return True
  return False

