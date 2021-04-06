
def divisible_by_left(n):
  A=[False]
  for i in range(1,len(str(n))):
    if int(str(n)[i-1]):
      if int(str(n)[i])%int(str(n)[i-1]):
        A.append(False)
      else:
        A.append(True)
    else:
      A.append(False)
  return A

