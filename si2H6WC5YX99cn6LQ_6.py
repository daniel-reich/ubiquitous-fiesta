
def sum_numbers(n):
  if n<2:
    return 1
  else :
    return (n+sum_numbers(n-1))

