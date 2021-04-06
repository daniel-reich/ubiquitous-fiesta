
def split(txt):
  stack=[]
  lst = []
  str = ''
  for char in txt:
    str = str + char
    if char == '(':
      stack.append(char)
    else:
      stack.pop()
      if not stack:
        lst.append(str)
        str =''
  return lst

