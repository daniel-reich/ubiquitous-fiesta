
def resist(net):
  di = {"[": "]", "(": ")"}
  while True:
    current = ""
    for i in range(len(net)):
      if net[i] in "[(": current = i
      if net[i] in "])" and di[net[current]] == net[i]: 
        current = [current, i+1]
        break
    if current == "": return round(float(net),1)
    else:
      evaluated = net[current[0]+1: current[1]-1]
      if net[current[0]] == "(": evaluated = sum([float(x) for x in evaluated.split(", ")])/1
      if net[current[0]] == "[": evaluated = 1/sum(([1/float(x) for x in evaluated.split(", ")]))
      net = net[:current[0]] + str(evaluated)+ net[current[1]:]

