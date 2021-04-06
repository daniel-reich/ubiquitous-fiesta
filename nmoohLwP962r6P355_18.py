
def straight_digital(number):
  if number < 100:
    return "Not Straight"
  digits = str(number)
  step = int(digits[1])-int(digits[0])
  for i in range(1,len(digits)-1):
    if int(digits[i+1]) - int(digits[i]) != step:
      return "Not Straight"
  if step == 0:
    return "Trivial Straight"
  else:
    return step

