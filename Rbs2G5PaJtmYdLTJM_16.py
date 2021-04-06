
def is_heteromecic(n):
  def pronic_generator(n):
    return n * (n+1)
  
  pronic_numbers = [-1]
  num = 0
  
  while max(pronic_numbers) < n:
    pronic_numbers.append(pronic_generator(num))
    num += 1
  
  return n in pronic_numbers

