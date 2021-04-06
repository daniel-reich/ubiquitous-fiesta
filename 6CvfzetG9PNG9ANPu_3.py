
def mubashir_cipher(message):
  key= [['m', 'c'], ['u', 'e'], ['b', 'g'], ['a', 'k'], ['s', 'v'], ['h', 'x'],['i', 'z'], ['r', 'y'], ['p', 'w'], ['l', 'n'], ['o', 'j'], ['t', 'f'], ['q', 'd']]
  key2 = []
  for x in key:
    key2.append([x[1], x[0]])
  fullkey = key + key2
  mydict = {}
  for n in fullkey:
    mydict[n[0]] = n[1]
  answer = ""
  for y in message:
    if y.isalpha() == True:
      answer += mydict[y]
    else:
      answer += y
  return answer

