
def cap_to_front(s):
  return ''.join([i for i in s if i.isupper()]+[i for i in s if i.islower()])

