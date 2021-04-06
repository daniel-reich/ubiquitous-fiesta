
def count_digits(lst, t):
  k = {'odd': '13579', 'even': '24680'}
  return [sum([str(x).count(i) for i in k[t]]) for x in lst]

