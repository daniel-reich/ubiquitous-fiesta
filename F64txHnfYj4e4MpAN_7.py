
def schoty(frame):
  def wire_count(wire):
    return len(wire.split('---')[0])
  
  result = 0
  for i in range(0, 7):
    result += pow(10, 6 - i) * wire_count(frame[i])
  return result

