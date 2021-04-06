
def is_repdigit(num):
  if num < 0 :
    return False
  elif num == 0 :
    return True
  else :
    a = list(map(int , str(num)))
    ans = set(a)
    return len(ans) == 1
​
​
print(is_repdigit(99))

