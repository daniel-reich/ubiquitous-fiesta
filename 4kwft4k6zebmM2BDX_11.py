
def chi_squared_test(data):
  e=data["E"]+[sum(data["E"])]
  t=data["T"]+[sum(data["T"])]
  s=[e[i]+t[i] for i in range(3)]
  fe=[((e[i]-e[2]*s[i]/s[2])**2)/(e[2]*s[i]/s[2]) for i in range(2)]
  ft=[((t[i]-t[2]*s[i]/s[2])**2)/(t[2]*s[i]/s[2]) for i in range(2)]
  x2=sum(fe)+sum(ft)
  if x2>6.635:
    return([round(x2,1), "Edabitin effectiveness = 99%"])
  elif x2>3.841:
    return([round(x2,1), "Edabitin effectiveness = 95%"])
  else:
    return([round(x2,1), "Edabitin is ininfluent"])

