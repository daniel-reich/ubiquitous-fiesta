
def seesaw(num):
  try:
    left = int(str(num)[:len(str(num))//2])
    right = int(str(num)[round(len(str(num))/2):])
    dct = {"left": left, "right": right}
    if left == right: return "balanced"
    return max(dct, key=dct.get)
  except:
    return "balanced"

