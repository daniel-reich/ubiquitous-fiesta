
def discount(n, txt):
  if txt: 
    txt = txt.split(", ")
    txt_percent = [1-float(i[:-1])/100 for i in txt if i[-1]=="%"]
    txt_substract = [float(i) for i in txt if i[-1]!="%"]
    for i in txt_percent:
      n *= i
    n -= sum(txt_substract)
  return round(n, 2)

