
def changeTypes(lst):
  answer = []
  for i in lst:
    if type(i) == type(3):
      if i % 2 == 0:
        answer.append(i+1)
      else:
        answer.append(i)
    if type(i) == type('hi'):
      answer.append(i.capitalize() + '!')
    if type(i) == type(True):
      if i:
        answer.append(False)
      else:
        answer.append(True)
  return answer

