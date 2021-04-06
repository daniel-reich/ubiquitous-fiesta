
import operator, re
def correct_signs(txt):
  ops = {'<': operator.lt, '>': operator.gt}
  opsRegex = re.compile(r'<|>')
  opsList = opsRegex.findall(txt)
  numList = [int(i) for i in re.split(' < | > ', txt)]
  
  for i in range(len(opsList)):
    if not ops[opsList[i]](numList[i], numList[i + 1]):
      return False
  return True

