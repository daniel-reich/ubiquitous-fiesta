
def to_list(num):
  return [int(x) for x in str(num)]
​
def to_number(lst): 
  return int("".join([str(i) for i in lst]))

