
def is_happy(n):
  if n in [1, 4]:
    return n == 1 or not n == 4
  else : return is_happy(sum([int(c)**2 for c in str(n)]))

