
def is_unprimeable(n):                    # The unprimeables
  """ To be unprimeable, when a digit of n is replaced by any digits from 0-9, it must not be prime """
  is_prime = lambda n: all(n%i for i in range(2, int(n**0.5)+1)) if n>2 and n%2 else n==2
  if is_prime(n): return "Prime Input"
  n = list(str(n))
  results = []
  for i, x in enumerate(n):
    for j in range(0, 10):
      num = int("".join(n[:i]) + str(j) + "".join(n[i+1:]))
      if is_prime(num): results.append(num)
  return "Unprimeable" if not results else sorted(results)

