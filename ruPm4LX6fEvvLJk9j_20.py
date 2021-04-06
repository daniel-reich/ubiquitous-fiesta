
def esthetic(num):
  l = []
  for i in range(2, 11):
    l.append(num_to_base(num, i))
  
  lst = []
  for i in range(len(l)):
    if all(abs(l[i][j] - l[i][j+1]) == 1 for j in range(len(l[i]) -1)):
      lst.append(i+2)
  return lst if lst else "Anti-Esthetic"
    
def num_to_base(n, b):
  digits = []
  if n == 0:
    return [0]
  
  while n:
    digits.append(int(n % b))
    n //= b
  return digits[::-1]

