
def expanded_form(num: float) -> str:
  gt1, lt1 = str(num).split('.')
  result = []
  for i in range(len(gt1)):
    if gt1[i] != '0':
      result.append(gt1[i] + '0' * (len(gt1) - 1 - i))
  for i in range(len(lt1)):
    if lt1[i] != '0':
      result.append(lt1[i] + '/1' + '0' * (i + 1))
  return ' + '.join(result)

