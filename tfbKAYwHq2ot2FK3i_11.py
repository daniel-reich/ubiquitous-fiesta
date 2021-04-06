
fact = lambda n: 1 if n<= 1 else n * fact(n-1)
def non_repeats(radix):
  return sum((fact(radix) * (radix-1)) // (radix * fact(radix-nd)) for nd in range(1, radix+1))

