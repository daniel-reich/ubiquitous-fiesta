
def seating_students(lst):
  l = lst[1:]
  p = lambda x: ((1 if (x>2 and x not in l and x-2 not in l) else 0)
              + (1 if (x%2==0 and x not in l and x-1 not in l) else 0))
  return sum([p(x) for x in range(1, lst[0]+1)])

