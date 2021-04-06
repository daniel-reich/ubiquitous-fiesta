
combintation = list()
a = [0, 3, 3, 3, 3, 3, 4, 3, 4]
def make_s(digits, string):
  if (len(string) == len(digits)):
    combintation.append(string)
  else:
    dc = int(digits[len(string)])
    f = 0
    for k in range(1,dc-1):
      f+=a[k]
​
    for i in range(f, f+a[dc-1]):
      make_s(digits,string+chr(97+i))
def letter_combinations(digits):
  combintation.clear()
  make_s(digits, "")
  print(combintation)
  return combintation

