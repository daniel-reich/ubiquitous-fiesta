
def bugger(num):
  count = 0
  while len(str(num)) > 1:
    digits = []
    for char in str(num):
      digits.append(int(char))
    total = 1
    for item in digits:
      total *= item
    num = total
    count += 1
  return count

