
def all_about_strings(txt):
  result = []
  result.append(len(txt))
  result.append(txt[0])
  result.append(txt[-1])
  if len(txt) % 2 == 0:
    result.append(txt[(len(txt) // 2) - 1] + txt[len(txt) // 2])
  else:
    result.append(txt[len(txt) // 2])
  if txt.count(txt[1]) == 1:
    result.append('not found')
  else:
    result.append('@ index ' + str(txt.rindex(txt[1])))
  return result

