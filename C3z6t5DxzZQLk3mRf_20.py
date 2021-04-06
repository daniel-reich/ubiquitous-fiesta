
def tune(lst):
  frequinces = [329.63, 246.94, 196, 146.83, 110, 82.41]
  result = []
  for index, string in enumerate(lst):
    if string == 0:
      result.append(" - ")
      continue
    difference = abs(frequinces[index] - string)/frequinces[index] * 100
    if 0.5 <= difference <= 2.5:
      if string < frequinces[index]:
        result.append(">+")
      else:
        result.append("+<")
    elif difference > 2.5:
      if string < frequinces[index]:
        result.append(">>+")
      else:
        result.append("+<<")
    else:
      result.append("OK")
  return result
  '''
1 (E) 329.63 Hz E4
2 (B) 246.94 Hz B3
3 (G) 196.00 Hz G3
4 (D) 146.83 Hz D3
5 (A) 110.00 Hz A2
6 (E) 82.41 Hz
'''

