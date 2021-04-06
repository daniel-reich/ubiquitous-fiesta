
def grab_number_sum(s):
  import re
  digit_regex = re.compile(r'(\d+)')
  numbers = digit_regex.findall(s)
  for x in range(len(numbers)):
      numbers[x] = int(numbers[x])
  return sum(numbers)

