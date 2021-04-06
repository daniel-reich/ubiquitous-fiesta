
def sum_round(num):
  result = ''
  for index, number in enumerate(reversed(str(num))):
    if int(number):
      result += ' ' + str(int(number) * 10 ** index)
  return result.strip()

