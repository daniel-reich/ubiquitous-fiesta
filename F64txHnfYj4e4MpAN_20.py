
def schoty(frame):
  ret = []
  for line in frame:
    line = line.split('-')[0]
    ret.append(str(len(line)))
  return int(''.join(ret).lstrip('0'))

