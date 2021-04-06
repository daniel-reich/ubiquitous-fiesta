
def numbers_range(ranges):
  outList = ""
  if not ranges:
    return outList
  startRange = ranges[0]
  endRange = ranges[0]
​
  for num in range(1, len(ranges)):
    if ranges[num] == ranges[num - 1] + 1:
      endRange = ranges[num]
    else:
      if startRange != endRange:
        if startRange + 1 < endRange:
          outList += str(startRange) + "-" + str(endRange) + ","
        else:
          outList += str(startRange) + "," + str(endRange) + ","
      else:
        outList += str(startRange) + ","
      startRange = ranges[num]
      endRange = ranges[num]
​
  if startRange != endRange:
    if startRange + 1 < endRange:
      outList += str(startRange) + "-" + str(endRange)
    else:
      outList += str(startRange) + "," + str(endRange)
  else:
    outList += str(startRange)
  return outList

