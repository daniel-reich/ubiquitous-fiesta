
def cap_to_front(s):
  return "".join([char for char in s if char.isupper()] + [char for char in s if char.islower()])

