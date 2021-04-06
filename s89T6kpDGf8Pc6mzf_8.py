
digit = {"0": "abcdef","1":"bc","2":"abdeg","3":"abcdg",
"4":"bcfg",
"5":"acdfg",
"6":"acdefg",
"7":"abc",
"8":"abcdefg",
"9":"abcfg"}
def seven_segment(txt):
  lst = []
  for i in range(0,len(txt)-1):
    lst.append(list(filter(lambda x: not x in digit[txt[i+1]],digit[txt[i]])))
    lst[-1].extend(list(map(lambda x: x.upper(),list(filter(lambda y: not y in digit[txt[i]],digit[txt[i+1]])))))
  for item in lst:
    item.sort(key = lambda x: x.lower())
  return lst

