
def negative_sum(chars):
  import re
  result = 0
  numb = re.findall('[-][0-9]?[0-9]',chars)
  for number in numb:
    result += int(number)
  return result

