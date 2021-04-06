
def insert_whitespace(s):
  res = ""
  for i in s:
    if i.isupper():
      res += " " + i
    else:
      res += i
​
  return (res.lstrip())

