
def calc(s):
  a = int("".join([str(ord(i)) for i in s]))
  return (([i for i in str(a)]).count('7'))*6

