
import re
def sentence(word):
  result = ''
  lst = ["an " + i if bool(re.match(r"[aeiou]", i)) else "a " + i for i in word]
  for i in range(len(word)):
    item = lst[i]
    if i == len(word) - 2:
       result += item + " and "
    elif i == len(word) - 1:
       result += item + "."
    else:
       result += item + ", "
  return result[0].upper() + result[1:]

