
def validate(s):
  valid = ["+x-xxx-xxx-xxxx", "xxx-xxx-xxxx", "x-xxx-xxx-xxxx", "(xxx) xxx-xxxx", "x (xxx) xxx-xxxx",   "xxx.xxx.xxxx", "x.xxx.xxx.xxxx", "x/xxx/xxx/xxxx", "x xxx xxx xxxx", "xxx/xxx/xxxx", "xxxxxxxxxxx","xxxxxxxxxx", "xxx xxx xxxx"]
  for i in "0123456789": s = s.replace(i, "x")
  for i in valid:
    if i == s: return True
  return False

