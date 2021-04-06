
def chi_squared_test(data):
  one,two,three,four = data["E"][0],data["E"][1],data["T"][0],data["T"][1]
  total = one+two+three+four
  one,two,three,four = (one+two)*(one+three)/total,(one+two)*(two+four)/total,(three+four)*(one+three)/total,(three+four)*(two+four)/total
  one,two,three,four = (one-data["E"][0])**2/one,(two-data["E"][1])**2/two,(three-data["T"][0])**2/three,(four-data["T"][1])**2/four
  chi2=one+two+three+four
  if chi2>6.635: return [round(chi2,1),"Edabitin effectiveness = 99%"]
  return [round(chi2,1),"Edabitin effectiveness = 95%"] if chi2>3.841 else [round(chi2,1),"Edabitin is ininfluent"]

