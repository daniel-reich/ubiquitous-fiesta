
def all_about_strings(txt):
  result = []
  result.append(len(txt))
  result.append(txt[0])
  result.append(txt[-1])
  if len(txt) % 2:
    result.append(txt[len(txt)//2])
  else:
    result.append(txt[(len(txt)//2)-1:(len(txt)//2)+1])
  if txt.rindex(txt[1]) == 1:
    result.append('not found')
  else:
    result.append('@ index {}'.format(txt.rindex(txt[1])))
  return result

