
def format_phone_number(lst):
  num = ''.join(map(str, lst))
  return "(%d) %d-%d" % (int(num[0:3]), int(num[3:6]), int(num[6:10]))

