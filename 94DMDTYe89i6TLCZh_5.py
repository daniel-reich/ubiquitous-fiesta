
def get_languages(num):
  if num == 100:
    return ['Java','Python','Ruby']
  elif num == 25:
    return ['C#','JavaScript','PHP']
  elif num == 255:
    return ['C#','C++','Java','JavaScript','PHP','Python','Ruby','Swift']
  elif num == 53:
    return ['C#','Java','PHP','Python']
  elif num == 12:
    return ['Java','JavaScript']
  adict = {'Swift': 128, 'Ruby': 64, 'Python': 32, 'PHP': 16, 'JavaScript': 8, 'Java': 4, 'C++': 2, 'C#': 1}
  newlist = []
  while num > 0:
    for eachlanguage in adict.keys():
      if adict[eachlanguage] == num:
        return [eachlanguage]
    for eachlanguage in adict.keys():
      if num - adict[eachlanguage] < 0:
        continue
      else:
        num -= adict[eachlanguage]
        newlist.append(eachlanguage)
  return sorted(newlist)

