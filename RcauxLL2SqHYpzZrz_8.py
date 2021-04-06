
def true_equations(lst):
  newlist = []
  for eachitem in lst:
    x = eachitem.split('=')
    answer = x[-1]
    equation = x[0]
    if eval(equation) == int(answer):
      newlist.append(eachitem)
  return newlist

