
def schoty(frame):
  temp_count = 0
  count_str = ""
  for wire in frame:
    for bead in wire:
      if bead == "-":
        count_str += str(temp_count)
        temp_count = 0
        break
      else:
        temp_count += 1
  print(count_str)
  return int(count_str)

