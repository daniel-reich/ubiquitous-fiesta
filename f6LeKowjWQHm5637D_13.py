
def cap_to_front(s):
  return ''.join([''.join([i for i in s if ord(i)>=65 and ord(i)<=90]),''.join([i for i in s if ord(i)>=97 and ord(i)<=122])])

