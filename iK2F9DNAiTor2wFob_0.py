
def calc(s):
  return len([1 for i in ''.join(str(ord(i)) for i in s) if i == '7']) * 6

