
def switcheroo(txt):
  chars = [i for i in txt]
  for i in range(len(chars)+3):
    if chars[i:i+3] == [i for i in 'nts'] and chars[i+3] in ' ,.!?': 
      chars[i:i+3] = [i for i in 'nce']
    elif chars[i:i+3] == [i for i in 'nce'] and chars[i+3] in ' ,.!?': 
      chars[i:i+3] = [i for i in 'nts']
  return ''.join(chars)

