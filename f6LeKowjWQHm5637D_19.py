
def cap_to_front(s):
  return "".join(list((x for x in s if x.isupper())) + list((x for x in s if x.islower())))

