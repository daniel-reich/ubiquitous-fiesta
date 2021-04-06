
def lychrel(n, count=0):
  if str(n) == ''.join(str(n)[::-1]):
    return count
  elif count == 500:
    return True
  else:
    return lychrel(n+int(''.join(str(n)[::-1])), count+1)

