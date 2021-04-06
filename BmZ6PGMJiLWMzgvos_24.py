
def check_parity(index, num):
  return (index%2 and num%2) or (not index%2 and not num%2)
​
def is_special_array(lst):
  return all(check_parity(i, n) for i, n in enumerate(lst))

