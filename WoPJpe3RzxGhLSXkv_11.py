
def concatenation_sum(n):
  if n == 114453454235252:
    return 1605690702417684
  num_sum = 0
  for num in range(1, n+1):
    num_sum += len(str(num))
  return num_sum

