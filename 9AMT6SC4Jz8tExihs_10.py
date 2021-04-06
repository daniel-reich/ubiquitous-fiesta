
def bin_l(n, l):
  return "{value:0{length:d}b}".format(value=n, length=l)
​
def all_strings(l):
  for n in range(0, 2 ** l):
    yield bin_l(n, l)
  
def generate_nonconsecutive(n):
    has_consecutive = lambda s : not any(g == ('1', '1') for g in zip(s, s[1:]))
    return ' '.join(filter(has_consecutive, all_strings(n)))

