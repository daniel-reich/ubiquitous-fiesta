
def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  result = ""
  for letter in message:
    if not letter.isalpha():
      result += letter
      continue
    for pair in key:
      if letter in pair:
        for l in pair:
          if letter != l:
            result += l
            break
  return result

