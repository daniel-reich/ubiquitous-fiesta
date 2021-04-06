
import re
​
dictio = {'11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e',
        '21': 'f', '22': 'g', '23': 'h', '24': 'i', '25': 'j', 
        '31': 'l', '32': 'm', '33': 'n', '34': 'o', '35': 'p',
        '41': 'q', '42': 'r', '43': 's', '44': 't', '45': 'u',
        '51': 'v', '52': 'w', '53': 'x', '54': 'y', '55': 'z'}
        
def dot_to_str(dots):
  pattern = '\.+\s{1}\.+'
  matches = re.findall(pattern, dots)
  res = ''
  for match in matches:
    num1, num2 = match.split()
    res += dictio[str(len(num1)) + str(len(num2))]
  return res
  
def str_to_dot(string):
  li = list(string)
  res = []
  for letter in string:
    if letter == 'k': 
      res.append('. ...')
      continue
    numDots = list(dictio.keys())[list(dictio.values()).index(letter)]
    res.append('.' * int(numDots[0]))
    res.append('.' * int(numDots[1]))
  return ' '.join(res)
  
def tap_code(text):
  if set(text) == {'.', ' '}: return dot_to_str(text)
  else: return str_to_dot(text)

