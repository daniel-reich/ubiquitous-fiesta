
import re
​
def sorting(s):
  numbers = re.findall(r'\d',s)
  letters = re.findall(r'\D',s)
  letters.sort(key = lambda x: ord(x.lower()))
  letters = ''.join(letters)
  numbers.sort()
  lst = list(map(lambda x: x.upper() + x.lower(), 'abcdefghijklmnopqrstuvwxyz'))
  for item in lst:
    letters = letters.replace(item,item[::-1])
  return ''.join(letters) + ''.join(numbers)

