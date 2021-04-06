
def return_end_of_number(num):
  s=str(num)
  for x in map(str,range(4,14)):
    if s.endswith(x):
      return s+"-TH"
  return "{}-{}".format(s,["ST","ND","RD"][int(s[-1])-1])

