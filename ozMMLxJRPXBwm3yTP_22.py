
def is_factorial(n):
      prod=1
      for div in range(2,20):
            prod=prod*div
            if prod==n: return True
            if prod>n: return False

