
def cleave(string, lst):
  index = 0
  answer = []
  while index < len(string):
    str2 = string[index:]
    count = 1
    while str2 not in lst and len(str2)>0:
      str2 = string[index:-count]
      count += 1
    if len(str2) == 0:
      answer = []
      break
    if str2 == 'as' and string[0] == 'f':
      answer.append(str2[:-1])
      index += len(str2[:-1])
    else:
      answer.append(str2)
      index += len(str2)
  if answer == []:
    return 'Cleaving stalled: Word not found'
  else:
    return ' '.join(answer)

