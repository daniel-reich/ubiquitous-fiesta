
def cap_to_front(s):
  o = ["",""]
  for i in s:
    o[i.islower()] += i
  return "".join(o)

