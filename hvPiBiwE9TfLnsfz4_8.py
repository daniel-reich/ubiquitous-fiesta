
def generate_word(n):
  def fib_seq(num_of_iters, b = None, a = None):
    if num_of_iters == 0:
      return []
    if b == None:
      b = 'b'
      return ['b'] + fib_seq(num_of_iters - 1, b, a)
    elif a == None:
      a = 'a'
      return [a] + fib_seq(num_of_iters - 1, b, a)
    else:
      return [b + a] + fib_seq(num_of_iters - 1, a, b + a)
  
  if n < 2:
    return 'invalid'
  
  else:
    return ', '.join(fib_seq(n))

