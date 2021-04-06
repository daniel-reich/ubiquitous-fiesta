
def mystery_func(num):
  temp = num
  resultS = ''
  while (temp >= 2):
    temp = temp/2
    resultS += '2'
  resultS += str(num-2**len(resultS))
  return int(resultS)

