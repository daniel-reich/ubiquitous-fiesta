
def calculate_scores(txt):
  if txt=="":
    return [0,0,0]
  else:
    a=txt.count("A")
    b=txt.count("B")
    c=txt.count("C")
    return [a,b,c]

