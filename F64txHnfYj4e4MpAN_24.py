
def schoty(frame):
  return int("".join(str(len(frame[i].split("-")[0])) for i in range(7)))

