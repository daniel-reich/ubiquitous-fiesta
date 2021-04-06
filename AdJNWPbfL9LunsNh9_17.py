
def multiplication_table(n):
  def multiplyn(x):
    def multiply(y):
      return x*y
    return multiply
  return [list(map(multiplyn(i),range(1,n+1))) for i in range(1,n+1)]

