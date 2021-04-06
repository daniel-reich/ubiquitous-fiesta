
def concat(*args):
  outputList = []
  for elements in args:
    for pieces in elements:
      outputList.append(pieces)
  return outputList

