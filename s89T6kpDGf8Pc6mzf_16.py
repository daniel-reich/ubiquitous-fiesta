
def seven_segment(txt):
  guide = {'0':'abcdef','1':'bc','2':'abdeg','3':'abcdg','4':'bcfg','5':'acdfg',
  '6':'acdefg','7':'abc','8':'abcdefg','9':'abcfg'}
  changes, temp = [], []
  for i in range(1,len(txt)):
    for j in 'abcdefg':
      if j in guide[txt[i]] and j not in guide[txt[i-1]]:
        temp.append(j.upper())
      elif j in guide[txt[i-1]] and j not in guide[txt[i]]:
        temp.append(j)
    changes.append(temp)
    temp = []
  return changes

