
def coloured_triangle(row):
  forms = {"RB":"G",
          "RG":"B",
          "BG":"R",
          "GB":"R",
          "GR":"B",
          "BR":"G",
          "BB":"B",
          "GG":"G",
          "RR":"R"}
​
  double, new = "", ""
  if len(row) == 1: return row
  while True:
    for id in range(len(row)-1):
      double += row[id]
      double += row[id+1]
      if len(double) == 2:
        new += forms[double]
        double = ""
    if len(new)>1:
      row = new
      new = ""
    else:
      return new

