
def total_volume(*boxes):
  if not boxes:
    return 0
  vt = 0
  for box in boxes:
    v = 1
    for l in box:
      v *= l
    vt += v
  return vt

