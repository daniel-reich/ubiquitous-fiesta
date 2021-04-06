
def mubashir_cipher(message):
  string = ""
  check = False
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  for i in message.lower():
    check = False
    for code in key:
      if i == code[0]:
        string += code[-1]
        check = True
      elif i == code[-1]:
        check = True
        string += code[0]
    if check == False:
      string += i
  return string

