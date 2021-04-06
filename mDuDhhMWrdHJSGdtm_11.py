
def is_exactly_three(n):
  sqrt = n**0.5
  if sqrt.is_integer() and sqrt != 1:
    for i in range(2,int(sqrt)):
      if sqrt % i == 0:
        return False
    return True
  return False

