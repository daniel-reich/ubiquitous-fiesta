
def left_slide(row):
  buffer = 0
  result = []
  for num in row:
    if num > 0 and num == buffer:
      result.append(2*num)
      buffer = 0
    elif num > 0 and buffer > 0 and num != buffer:
      result.append(buffer)
      buffer = num
    elif buffer == 0 and num > 0:
      buffer = num
  if buffer > 0:
    result.append(buffer)
  result += [0] * (len(row) - len(result))
  return result

