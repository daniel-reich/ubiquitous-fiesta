
def seesaw(num):
  if len(str(num)) == 1 or num is None:
    return "balanced"
  num = str(num)
  if len(num) % 2 != 0:
    half = int((len(num) - 1) / 2)
    num = num[:half] + num[half +1:]
  length = int(len(num) / 2)
  if int(num[:length]) > int(num[length:]):
    return "left"
  if int(num[:length]) < int(num[length:]):
    return "right"
  return "balanced"

