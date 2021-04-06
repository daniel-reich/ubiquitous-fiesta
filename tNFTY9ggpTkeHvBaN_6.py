
def total_volume(*boxes):
  vol=0
  for box in boxes:
    vol += box[0]*box[1]*box[2]
  return vol

