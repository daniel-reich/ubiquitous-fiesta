
def return_end_of_number(num):
  
  if (num == 1):
    return "1-ST"
  elif (num == 2):
    return "2-ND"
  elif (num == 3):
    return "3-RD"
  elif (num >= 4) and (num <= 9):
    return str(num) + "-TH"
  
  elif (str(num)[-1] == "1") and (str(num)[-2] == "1"):
    return str(num) + "-TH"
  elif (str(num)[-1] == "1") and (str(num)[-2] != "1"):
    return str(num) + "-ST"
  
  elif (str(num)[-1] == "2") and (str(num)[-2] == "1"):
    return str(num) + "-TH"
  elif (str(num)[-1] == "2") and (str(num)[-2] != "1"):
    return str(num) + "-ND"
  
  elif (str(num)[-1] == "3") and (str(num)[-2] == "1"):
    return str(num) + "-TH"
  elif (str(num)[-1] == "3") and (str(num)[-2] != "1"):
    return str(num) + "-RD"
  
  else:
    return str(num) + "-TH"

