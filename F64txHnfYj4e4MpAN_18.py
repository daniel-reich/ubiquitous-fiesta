
def schoty(frame):
  return int(''.join([str(len(f.split("---")[0])) for f in frame]).lstrip("0"))

