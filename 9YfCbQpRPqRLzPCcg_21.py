
def will_hit(equation, position):
  eq_lst = equation.split(' ')
  m = int(str(eq_lst[2])[:-1])
  c = int(eq_lst[-1])
  if '-' in eq_lst:
    return position[1] == m * position[0] - c
  return position[1] == m * position[0] + c

