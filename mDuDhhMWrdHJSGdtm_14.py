
def is_exactly_three(n):
  if (n**0.5)%1 != 0:
    return False
  else:
    a = int(n**0.5)
    if a > 1:
      for i in range(2, a):
        if (a % i) == 0:
          return False
          break
      else:
        return True
    else:
      return False

