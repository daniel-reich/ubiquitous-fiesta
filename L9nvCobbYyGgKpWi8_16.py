
def to_list(num):
  return [int(x) for x in str(num)] 
​
def to_number(lst):
  ls = [str(element) for element in lst]
  return int("".join(ls))

