
def seesaw(num):
  if num and num > 9:
    i = len(str(num))//2
    if int(str(num)[:i]) > int(str(num)[-i:]):
      return "left"
    if int(str(num)[:i]) < int(str(num)[-i:]):
      return "right"
  return "balanced"

