
def count_digits(lst, t):
  return [sum([int(x)%2 if t=='odd' else int(x)%2==0 for x in str(x)]) for x in lst]

