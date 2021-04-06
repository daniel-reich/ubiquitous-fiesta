
def cap_to_front(s):
  return "".join([x for x in s if x.isupper()] + [x for x in s if x.islower()])

