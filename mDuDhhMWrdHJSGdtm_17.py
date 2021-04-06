
def is_exactly_three(n):
  sqrt = n**.5
  if sqrt == round(sqrt) and n != 1:
    is_three = True
    for i in range(2,int(sqrt)):
      if sqrt%i == 0:
        is_three = False
        break
  else:
    is_three = False
  return is_three

