
def scale_tip(lst):
  idx = lst.index("I")
  left, right = sum(lst[:idx]), sum(lst[idx+1:])
  if left > right: return "left"
  elif left < right: return "right"
  else: return "balanced"

