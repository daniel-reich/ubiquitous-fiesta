
def eval_factorial(lst):
  def fact(n):
    return 1 if n<=1 else n*fact(n-1)
  return sum(fact(int(n[:-1])) for n in lst)

