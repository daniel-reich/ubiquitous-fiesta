
def quad_sequence(lst):
  a = 0
  b = 0
  c = 0
  constant = lst[0]
  first_difference = lst[1] - lst[0] 
  second_difference = (lst[2]-lst[1])-(first_difference)
  a = second_difference/2
  b = first_difference - 3*a
  c = constant - a - b
  for x in range (len(lst)+1, len(lst)*2+1):
    total = 0
    total = a*(x**2) + b*x + c
    lst[x - len(lst)-1] = total
  return(lst)

