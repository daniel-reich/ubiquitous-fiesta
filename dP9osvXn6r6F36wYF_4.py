
def front3(text):
  if len(text) < 3:
    prefix = text
  else:
    prefix = text[:3]
  return prefix*3

