
def route_diff(d):
  return len(d)-abs(d.count('S')-d.count('N'))-abs(d.count('W')-d.count('E'))

