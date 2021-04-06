
def domino_chain(dominos):
  output = ''
  seen = []
  for i in range(len(dominos)):
    if dominos[i] == '|' and ' ' not in seen and '/' not in seen:
      output += '/'
      seen.append(dominos[i])
    else:
      output += dominos[i]
      seen.append(dominos[i])
  return output

