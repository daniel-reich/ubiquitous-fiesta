
def all_prime(lst):
  def prime(n):
    return all([(n%j) for j in range(2,int(n**0.5)+1)]) and n>1
  result = list(map(prime,lst))
  return True if len(list(set(result))) == 1 else False

