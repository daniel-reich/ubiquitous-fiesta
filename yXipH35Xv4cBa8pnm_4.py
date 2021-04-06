
def microwave_buttons(time):
  x = time.split(':')
  if (int(x[1]) % 30 == 0 and x[1] != '00'):
    return int(int(x[1])/30) + 1
  if len(set(time)) == 2:
    return 1
  if (x[0][0] == '0'):
    return 3
  if (x[0][1] == '0'):
    return 5
  if (x[1][0] == '0'):
    return 2
  return 3

