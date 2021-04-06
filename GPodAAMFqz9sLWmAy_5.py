
def one_odd_one_even(n):
  return (n%2 and not n//10 % 2) or (not n%2 and n//10 % 2)

