
def gcd(arr):
  def find_factors(num):
    return list(reversed([n for n in range(2, num+1) if num % n == 0] ))
  
  all_divisors = [find_factors(n) for n in arr]
  shortest = [div for div in all_divisors if len(div) == min([len(d) for d in all_divisors])][0]
  
  for n in range(len(shortest)):
    item = shortest[n]
    print(item)
    poss = True
    for divisor in all_divisors:
      if item not in divisor:
        poss = False
        break
    if poss == True:
      return item
  
  return 1

