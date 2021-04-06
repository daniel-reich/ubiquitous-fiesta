
def solver(eq):
  c = eval(eq.replace('=', '-(') + ')', {"x": 1j})
  try:  
    return -c.real / c.imag
  except ZeroDivisionError:
    return "Infinite solutions"

