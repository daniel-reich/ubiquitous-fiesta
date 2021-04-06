
def cap_to_front(s):
  n = "".join([l for l in s if l.islower() == False])
  n2 = "".join([l for l in s if l.islower() == True])
  return n + n2

