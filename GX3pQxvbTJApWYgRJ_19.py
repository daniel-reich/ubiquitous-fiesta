
def is_kaprekar(n):
  
  if len(str(n ** 2)) == 1:
    return 0 + (n ** 2) == n
  else:
    return int(str(n ** 2)[:len(str(n ** 2))//2]) + int(str(n ** 2)[len(str(n ** 2))//2:]) == n

