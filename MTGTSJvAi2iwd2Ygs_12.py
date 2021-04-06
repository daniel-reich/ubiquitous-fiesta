
def valid_division(d):
  return 'invalid' if d[-1] == '0' else eval(d.replace('/','%')) == 0

