
def bemirp(n):                        # I Put My Prime Down, Flip It and Reverse It
  """ Return if n is prime, flipped prime, reversed prime and flipped reversed prime """
  is_prime = lambda n: all(n%i for i in range(2, int(n**0.5)+1)) if n>2 and n%2 else n==2
  is_ermip = lambda n: n!=int(str(n)[::-1]) and is_prime(n) and is_prime(int(str(n)[::-1]))
  flipped = lambda n: int("".join([x if x not in "69" else "6" if x=="9" else "9" for x in str(n)]))
  is_bermip = lambda n: all(x not in "23457" for x in str(n)) and is_ermip(n) and is_ermip(flipped(n))
  return "B" if is_bermip(n) else "E" if is_ermip(n) else "P" if is_prime(n) else "C"

