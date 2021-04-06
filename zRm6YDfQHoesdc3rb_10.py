
def rectangles(step):
  if step == 0:
    return 0
  if step == 1:
    return 1 
  return step ** 3 + rectangles(step - 1)

