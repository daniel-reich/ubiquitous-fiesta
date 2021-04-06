
def to_list(num):
  return [int(n) for n in str(num)]
​
def to_number(lst):
  return int(''.join([str(n) for n in lst]))

