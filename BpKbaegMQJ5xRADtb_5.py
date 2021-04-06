
def is_unprimeable(num):
  if check_prime(num):
    return "Prime Input"
  else:
    num = str(num)
    arr = []
    for i in range(len(num)):
      for j in range(0, 10):
        if check_prime(int(num[0:i]+str(j)+num[i+1::])):
          arr.append(int(num[0:i]+str(j)+num[i+1::]))
    if not arr:
      return 'Unprimeable'
    else:
      return sorted(arr)
  
  
def check_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

