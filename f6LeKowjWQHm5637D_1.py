
def cap_to_front(s):
  uppers = [i for i in s if i.isupper()]
  lowers = [i for i in s if i.islower()]
  return "".join(uppers + lowers)

