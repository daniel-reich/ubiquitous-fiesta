
def one_odd_one_even(n):
  return (((n//10)%2 == 0) and ((n%10)%2 == 1)) or (((n//10)%2 == 1) and ((n%10)%2 == 0))

