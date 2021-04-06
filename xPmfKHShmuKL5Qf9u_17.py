
def scale_tip(lst):
  tilt = ["left", "right", "balanced"]
  middle = lst.index("I")
  b = 0
  b += int(sum(lst[:middle]) <= sum(lst[middle + 1:]))
  b += int(sum(lst[:middle]) == sum(lst[middle + 1:]))
  return tilt[b]

