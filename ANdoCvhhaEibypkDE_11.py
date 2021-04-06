
def closing_in_sum(n):
  str_number = str(n)
  total = 0
  while len(str_number) > 1:
    total += int((str_number[0] + str_number[-1]))
    str_number = str_number[1:-1]
  try:
    total += int(str_number[0])
  except Exception as ex:
    return total
  return total

