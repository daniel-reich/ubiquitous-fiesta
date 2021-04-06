
def share(a,b):
  return set(str(a)) & set(str(b))
​
def shared_digits(l):
  for i in range(len(l)-1):
    if not share(l[i],l[i+1]):
      return False
  return True

