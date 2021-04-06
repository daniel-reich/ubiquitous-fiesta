
cuban_prime = lambda n: str(n) + ' is' + [' not ', ' '][2 in
  [n, 2**n % n] and not (3 + (12*n-3)**0.5) % 6] + 'cuban prime'

