
def ruth_aaron(n):
  def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
      if n % i:
        i += 1
      else:
        n //= i
        factors.append(i)
    if n > 1:
      factors.append(n)
    return factors
​
  distinct_pf_n0, distinct_pf_n1, distinct_pf_n2 = set(prime_factors(n)), set(prime_factors(n+1)), set(prime_factors(n-1))
  repeated_pf_n0, repeated_pf_n1, repeated_pf_n2 = prime_factors(n), prime_factors(n+1), prime_factors(n-1)
  result = []
  condition = [False, False, 'Type']
  if sum(distinct_pf_n0) == sum(distinct_pf_n1):
    condition[0] = True
    condition[2] = 'Ruth'
  if sum(distinct_pf_n0) == sum(distinct_pf_n2):
    condition[0] = True
    condition[2] = 'Aaron'
  if sum(repeated_pf_n0) == sum(repeated_pf_n1):
    condition[1] = True
    condition[2] = 'Ruth'
  if sum(repeated_pf_n0) == sum(repeated_pf_n2):
    condition[1] = True
    condition[2] = 'Aaron'
  if condition[0] and not condition[1]:
    result.append(condition[2])
    result.append(1)
  if not condition[0] and condition[1]:
    result.append(condition[2])
    result.append(2)
  if condition[0] and condition[1]:
    result.append(condition[2])
    result.append(3)
  if not condition[0] and not condition[1]:
    result = False
​
  return result

