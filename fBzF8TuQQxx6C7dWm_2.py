
def add(char, txt):
#Per request of test 3, .join() will be used; .replace() would also work
  if txt==" ":
    return char
  return char.join(txt.split())

