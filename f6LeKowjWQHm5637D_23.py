
def cap_to_front(s):
  return "".join([i for i in s if i == i.upper()]) + "".join([i for i in s if i == i.lower()])

