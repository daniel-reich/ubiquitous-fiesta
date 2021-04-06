
def inator_inator(inv):
  if inv[-1].lower() == "a" or inv[-1].lower() == "e" or inv[-1] == "i" or inv[-1]=="o" or inv[-1]=="u":
    return inv+"-inator "+str(len(inv))+"000"
  else:
    return inv+"inator " + str(len(inv))+"000"

