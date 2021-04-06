
def pie_chart(data):
  arrVal = []
  arrKey = []
  resultDict = {}
  multiplier = 0
  for val in data.values():
     arrVal.append(val)
  for key in data.keys():
     arrKey.append(key)
​
  total = 0
  for i in range(len(arrVal)):
      total += arrVal[i]
​
  multiplier = 360 / total
​
  for i in range(len(arrVal)):
      valCalc = round((arrVal[i] * multiplier), 1)
      if valCalc.is_integer():
          resultDict[arrKey[i]] = int(valCalc)
      else:
          resultDict[arrKey[i]] = valCalc
  return resultDict

