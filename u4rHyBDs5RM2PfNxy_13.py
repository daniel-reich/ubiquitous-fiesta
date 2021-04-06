
def count_ones(lst):
  return sum(1 for i in ''.join(map(str, lst)).split('0') if i.count('1')>1)

