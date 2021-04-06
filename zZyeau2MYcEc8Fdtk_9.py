
def round_number(num, n):
  if num%n>=(n/2):return n*(num//n) + n
  else: return n*(num//n)

