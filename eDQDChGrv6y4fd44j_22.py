
def can_put(txt, dim):
  text = txt.split()
  currentLineLength = len(text[0])
  
  if currentLineLength > dim[1]:
    return False
  
  currentRowCount = 0
  for word in text[1:]:
  
    if len(word) > dim[1]:
      return False
  
    if currentLineLength + len(word) + 1 > dim[1]:
      currentRowCount += 1
      currentLineLength == len(word)
    else:
      currentLineLength = currentLineLength + len(word) + 1
  
  if currentLineLength != 0:
    currentRowCount += 1
  
  return currentRowCount <= dim[0]

