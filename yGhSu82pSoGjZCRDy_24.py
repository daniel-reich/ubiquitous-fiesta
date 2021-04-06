
def seesaw(num):
  string = str(num)
  if len(string) == 1 or len(string) == 0 or num == None:
    return 'balanced'
  else:
    length = len(string) // 2
    l_s = string[:length]
    r_s = string[0-length:]
    if int(l_s) > int(r_s):
      return 'left'
    elif int(l_s) < int(r_s):
      return 'right'
    elif int(l_s) == int(r_s):
      return 'balanced'

