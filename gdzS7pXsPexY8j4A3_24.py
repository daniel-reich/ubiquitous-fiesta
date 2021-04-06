
def count_digits(lst, t):
  if t is 'odd':
    return [sum([1 for i in str(j) if int(i)%2]) for j in lst]
  else:
    return [sum([1 for i in str(j) if int(i)%2==0]) for j in lst]

