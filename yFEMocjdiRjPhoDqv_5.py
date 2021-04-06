
def prime_in_range(n1, n2):
  prime_lst = []
  for i in range(n1, n2 + 1):
    prime = True
    if i == 1:
      prime = False
    elif prime == 2:
      prime = True
    else:
      for j in range(2, i):
        if i % j == 0:
          prime = False
          break
    if prime == True:
      prime_lst.append(i)
  if len(prime_lst) != 0:
    return True
  else:
    return False

