
def convert(deg):
  return "{0}*F".format(round(int(deg[:-2]) * 9/5 + 32)) if (deg.split("*")[-1] == "C") else "{0}*C".format(round((int(deg[:-2]) - 32)*5/9)) if (deg.split("*")[-1] =="F") else "Error"

