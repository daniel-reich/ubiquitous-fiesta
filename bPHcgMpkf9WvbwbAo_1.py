
def format_phone_number(lst):
  s = "".join(map(str, lst))
  return "({}) {}-{}".format(s[0:3], s[3:6], s[6:])

