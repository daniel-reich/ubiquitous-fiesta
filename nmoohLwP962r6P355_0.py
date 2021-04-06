
def straight_digital(n):
  if n > 99:
    lst = [int(i) for i in str(n)]
    if len(set(lst)) == 1:
      return 'Trivial Straight'
    elif len(set(a-b for a,b in zip(lst,lst[1:]))) == 1:
      return lst[1]-lst[0]
  return 'Not Straight'

