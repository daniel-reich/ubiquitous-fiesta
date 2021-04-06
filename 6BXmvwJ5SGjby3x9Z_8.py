
def hours_passed(time1, time2):
  
  Text_A = time1.replace(" ",":")
  Text_B = time2.replace(" ",":")
  
  Blocks_A = Text_A.split(":")
  Blocks_B = Text_B.split(":")
  
  if (Blocks_A[-1] == "PM"):
    Hours_A = int(Blocks_A[0]) + 12
  elif (Blocks_A[0] == "12") and (Blocks_A[-1] == "AM"):
    Hours_A = 0
  else:
    Hours_A = int(Blocks_A[0])
  
  if (Blocks_B[-1] == "PM"):
    Hours_B = int(Blocks_B[0]) + 12
  else:
    Hours_B = int(Blocks_B[0])
  
  Elapsed = abs(Hours_A - Hours_B)
  
  if (Elapsed == 0):
    return "no time passed"
  else:
    return "{} hours".format(Elapsed)

