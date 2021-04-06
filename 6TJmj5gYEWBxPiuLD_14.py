
def seating_students(lst):
  a = lst[0] + 1
  desks = lst[1:]
  ways = 0
  for i in range(1, a):
    if i not in desks:
      if i + 1 not in desks and i + 1 < a and i % 2 == 1:
        ways += 1
      if i + 2 not in desks and i + 2 < a and i % 2 == 1:
        ways += 1
      if i + 2 not in desks and i + 1 < a and i % 2 == 0:
        ways += 1   
  return ways

