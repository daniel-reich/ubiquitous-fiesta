
def is_exactly_three(n):
  x = n**0.5
  return x == x//1 and all(x%i for i in range(2,int(x/2)+1)) and n!=1

