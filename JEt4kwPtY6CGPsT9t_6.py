
def mathematical(exp, numbers):
  answers = []
  for num in numbers:
    expression = exp.replace('y', str(num))
    equation, call = expression.split('=')[1], expression.split('=')[0]
    
    if 'x' in equation:
      equation = equation.replace('x', '*')
      
    if '^' in equation:
      equation = equation.replace('^', '**')
      
    answers.append('{0}={1:.0f}'.format(call, eval(equation)))
    
  else:
    return answers

