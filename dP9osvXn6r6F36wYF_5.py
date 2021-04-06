
def front3(text):
  front_end = 3
  if len(text) < front_end:
    front_end = len(text)
  front = text[:front_end]
  return front + front + front

