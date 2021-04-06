
def wiggle_string(s):
  tr = []
  
  for n in range(0, len(s)+1):
    string = ''
    for num in range(n):
      string += ' '
    string += s
    tr.append(string)
  
  for n in reversed(range(0, len(s))):
    string = ''
    for num in range(n):
      string += ' '
    string += s
    tr.append(string)
  
  return tr

