
from string import ascii_lowercase
​
def decrypt(s):
  numbers = []
  for c in s:
    if c == "#":
      # if hash, pop the last two numbers and combine them
      num = numbers.pop() + 10 * numbers.pop()
    else:
      # otherwise, just take the number value   
      num = int(c)
    numbers.append(num)
  # convert numbers to string
  return "".join([ascii_lowercase[n-1] for n in numbers])

