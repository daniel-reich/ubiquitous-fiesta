
def schoty(frame):
  positions = [wire.find('-') for wire in frame]
  value = ''.join(map(str, positions))
  print(value)
  return int(value)

