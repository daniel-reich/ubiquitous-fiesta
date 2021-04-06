
def scale_tip(lst):
  balance = sum([lst[i] if i < (len(lst) + 1) / 2 else -lst[i] for i in range(len(lst)) if type(lst[i]) == int])
  return "left" if balance > 0 else "right" if balance < 0 else "balanced"

