
def percent_filled(box):
  a = sum([1 for i in box for j in i if j==" "])
  b = sum([1 for i in box for j in i if j=="o"])
  return "{}%".format(round(b/(a+b)*100))

