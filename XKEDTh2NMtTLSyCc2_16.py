
def valid_credit_card(number):
  if len(str(number)) == 16:
    y = [int(char) for char in str(number)[::-1]]
    for i in range(16):
      if i%2:
        y[i] = y[i]*2
      if y[i] > 9:
        y[i] = y[i] - 9
    if not sum(y)%10:
      return True
    else:
      return False
  else:
    return True

