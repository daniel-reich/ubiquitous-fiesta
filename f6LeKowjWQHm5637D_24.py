
def cap_to_front(s):
  return "".join(sorted(list(s), key=lambda x: ord(x) >= 90))

