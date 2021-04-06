
def to_list(num):
  return [int(i) for i in str(num)]
​
def to_number(lst):
  y = [str(i) for i in lst]
  return int("".join(y))

