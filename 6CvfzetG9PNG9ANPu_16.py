
def mubashir_cipher(message):
  keys= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  result = ""
  for char in message:
    if 'a' <= char <= 'z':
      for lst in keys:
        if char == lst[0]:
          result += lst[1]
          break
        elif char == lst[1]:
          result += lst[0]
          break
    else:
      result += char
  return result

