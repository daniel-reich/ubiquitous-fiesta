
def digital_vowel_ban(digit, v):
​
  numbers = {1:"one", 2:"two", 3:"three", 4:"four",
    5:"five", 6:"six", 7:"seven", 8:"eight",
    9:"nine", 0:"zero",
    }
  l = []
  for i in str(digit):
    i = int(i) 
    if v in numbers.get(i):
      pass
    else:
      l.append(i)
  l = "".join([str(i) for i in l])
  if l == "":
    return "Banned Number"
  else:
    l = int(l)
    return l

