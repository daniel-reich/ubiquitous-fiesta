
def discount(num, txt):
  lst = txt.split(",")
  per = list()
  dis = list()
  if txt == "": return num
  for item in lst:
    if item[-1] == "%":
      per.append(item)
    else: dis.append(item)
  for item in per:
    num = num - num*float(item[:-1])/100
  for item in dis:
    num -= float(item)
  return round(num,2)

