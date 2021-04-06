
def is_consecutive(s):
  maxSteps = len(s)
  stepper = 1
  while stepper < maxSteps:
    consADJ = 0
    consADJList = []
    decConsADJList = []
    for i in range(0, len(s), stepper):
      if consADJ == 0:
        consADJ = int(s[i:i+stepper])
        consADJList.append(True)
        decConsADJList.append(consADJ)
      if i != 0:
          if int(s[i:i+stepper])-consADJ == -1 or int(s[i:i+stepper])-consADJ == 1:
              consADJList.append(True)
              consADJ = int(s[i:i+stepper])
              val = decConsADJList[0]-int(s[i:i+stepper])
              if val < 0: val *= -1
              decConsADJList.append(val)
          else:
              consADJList.append(False)
    if consADJList.count(True) == len(consADJList):
        for i in range(1, maxSteps+1):
            if i < len(decConsADJList):
                if i != decConsADJList[i]:
                    return False
        return True
    stepper += 1
  return False

