
def seven_segment(txt):
  code = {
    '0' : 'abcdef',
    '1' : 'bc',
    '2' : 'abdeg',
    '3' : 'abcdg',
    '4' : 'bcfg',
    '5' : 'acdfg',
    '6' : 'acdefg',
    '7' : 'abc',
    '8' : 'abcdefg',
    '9' : 'abcfg'
  }
  
  changes = []
  for i in range(1, len(txt)):
    changes.append(sorted([n.upper() for n in code[txt[i]] if n not in code[txt[i-1]]] + [n for n in code[txt[i-1]] if n not in code[txt[i]]], key=str.casefold))
​
  return changes

