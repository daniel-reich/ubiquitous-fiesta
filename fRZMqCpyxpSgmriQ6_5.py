
def sorting(s):
  li = list(s)
  li.sort(key=sorter)
  return ''.join(li)
  
  
def sorter(elem):
  if elem.isalpha():
    if elem.islower():
      return ord(elem.upper()) - 0.5
    else:
      return ord(elem)
  else:
    return ord(elem) + 43

