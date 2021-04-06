
import string
​
def sorting(s):
  init = sorted(s)
  numbers = []
  no_digit = []
​
  # store numbers
  for i in init:
    if i.isdigit():
      numbers.extend(i)
​
  # remove numbers from original string
  for i in init:
    if not i.isdigit():
      no_digit.extend(i)
​
  first_sort = sorted(no_digit, key=string.ascii_letters.index)
  final = sorted(first_sort, key=str.lower)
​
  # makes lists to string
  digit = "".join(numbers)
  new_s = "".join(final)
  
  return new_s+digit

