
def build_staircase(height, block):
  reslt_arry = []
  for i in range(1,height+1):
    tmp_arry = []
    tmp_arry = [block]*i + ['_']*(height-i)
    reslt_arry.append(tmp_arry)
  return reslt_arry

