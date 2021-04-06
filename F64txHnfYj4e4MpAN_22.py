
def schoty(frame):
  sum = 0
  index = 0
  conversion = [1000000, 100000, 10000, 1000, 100, 10, 1]
  for line in frame:
    sum = sum + conversion[index] * line.find("-")
    index = index + 1
  return sum

