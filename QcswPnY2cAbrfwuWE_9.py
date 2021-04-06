
def filter_factorials(numbers):
  return [i for i in numbers if isfact(i)]
def isfact(n):
  i = 1
  while(True):
    if n%i == 0:
      n//=i
    else:
      break
    i+=1
  if n==1:
    return True
  else: 
    return False

