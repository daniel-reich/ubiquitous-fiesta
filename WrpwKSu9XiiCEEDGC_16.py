
def can_alternate(s):
  one_count = [i for i in s if i == '1']
  zero_count = [i for i in s if i == '0']
  return abs(len(one_count) - len(zero_count)) <= 1

