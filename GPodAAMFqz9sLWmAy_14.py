
def one_odd_one_even(n):
  a = list(str(n))
  odd,even = 0,0
  for i in a:
    if int(i) % 2 == 0:
      even = even + 1
    else:
      odd = odd + 1
  if odd == even:
    return True
  else:
    return False

