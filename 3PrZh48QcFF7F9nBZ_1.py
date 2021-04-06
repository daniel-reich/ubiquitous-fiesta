
def solver(eq):
  
  eq = eq.replace('=', '==')
  solutions = []
  
  for x in range(-100, 101):
    if eval(eq) == True:
      solutions.append(x)
  
  if len(solutions) > 1:
    return 'Infinite solutions'
  elif len(solutions) == 1:
    return solutions[0]
  else:
    return 'Infinite solutions'

