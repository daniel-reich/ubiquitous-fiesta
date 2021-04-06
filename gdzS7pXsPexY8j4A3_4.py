
def count_digits(lst, t):
  lst = map(str, lst)
  return [sum([1 if (t == 'odd' and int(y)%2!=0) or (t == 'even' and int(y)%2==0) else 0 for y in x]) for x in lst]

