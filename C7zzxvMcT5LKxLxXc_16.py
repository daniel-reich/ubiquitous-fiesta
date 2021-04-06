
def decode(txt):
  result = []
  for char in txt:
    sum = 0
    for digit in str(ord(char)):
      sum += int(digit)
    result.append(sum)
  return result

