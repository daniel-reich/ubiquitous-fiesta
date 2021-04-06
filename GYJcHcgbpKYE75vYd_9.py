
def return_end_of_number(num):
  d = {
    1 : "ST",
    2 : "ND",
    3 : "RD",
    4 : "TH",
  }
  
  try :
    last = int(str(num)[-2:])
    if last > 10 and last < 14:
      return "{}-{}".format(num,"TH")
    else : return "{}-{}".format(num,d[int(str(num)[-1])])
  except :
    last = int(str(num)[-1])
    return "{}-{}".format(num,d[last])

