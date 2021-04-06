
def shared_digits(lst):
  s = [set(str(n)) for n in lst]
  return all([s[i] & s[i+1] != set() for i in range(len(s)-1)])

