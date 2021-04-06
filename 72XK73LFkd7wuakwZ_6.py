
def junction_or_self(n):
  test = lambda n: n + sum(int(d) for d in str(n))
  
  options = [k for k in range(n) if test(k)==n]
  
  return options[::-1] if options else "Self"

