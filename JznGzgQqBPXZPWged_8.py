
def resistCalc(net):
  tot = 0
  if net[0] == -1:
    for x in net[1:]:
      if isinstance(x, list): 
        tot += resistCalc(x)
      else:
        tot+=x
    return tot
  else:
    for x in net:
      if isinstance(x, list): 
        tot += 1/resistCalc(x)
      else:
        tot+=1/x
    return 1/tot
​
def resist(net):
  print(net)
  netList = eval(net.replace('(',"[-1,").replace(')',']'))
  return round(resistCalc(netList),1)

