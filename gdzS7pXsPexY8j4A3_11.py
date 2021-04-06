
def count_digits(lst, t):
  return [digit(n,t) for n in lst]  
​
def digit(num, t):
  s, count = str(num), 0
  for d in s:
    if t == "odd":
      if int(d)%2: count += 1
    if t == "even":
      if int(d)%2 == 0: count += 1
  return count

