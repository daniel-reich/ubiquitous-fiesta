
base = {'black': ['0', '0', '-', '-'], 'brown': ['1', '1', '+/-1%', '100ppm/k'], 'red': ['2', '2', '+/-2%', '50ppm/k'], 'orange': ['3', '3', '-', '15ppm/k'], 'yellow': ['4', '4', '-', '25ppm/k'], 'green': ['5', '5', '+/-0.5%', '-'], 'blue': ['6', '6', '+/-0.25%', '10ppm/k'], 'violet': ['7', '7', '+/-0.1%', '5ppm/k'], 'gray': ['8', '8', '+/-0.05%', '-'], 'white': ['9', '9', '-', '-'], 'gold': ['-', '-1', '+/-5%', '-'], 'silver': ['-', '-2', '+/-10%', '-']}
​
def remove_zeros(string):
  if "." in string:
    while string[-1] == "0":
      string = string[:-1]
    if string[-1] == ".":
      string = string[:-1]
  return string
​
def res(resistance):
  if resistance >= 10**9:
    return remove_zeros(str(resistance/10**9)) + "GOhm"
  if resistance >= 10**6:
    return remove_zeros(str(resistance/10**6)) + "MOhm"
  if resistance >= 10**3:
    return remove_zeros(str(resistance/10**3)) + "kOhm"
  return str(resistance) +"Ohm"
​
def resistor_code(colors):
  if len(colors) == 4:
    digit = int(base[colors[0]][0] + base[colors[1]][0])
    magnitude = 10**int(base[colors[2]][1])
    resistance = res(digit * magnitude)
    tolerance = base[colors[3]][2]
    return resistance + " " + tolerance
  elif len(colors) == 5:
    digit = int(base[colors[0]][0] + base[colors[1]][0]+ base[colors[2]][0])
    magnitude = 10**int(base[colors[3]][1])
    resistance = res(digit * magnitude)
    tolerance = base[colors[4]][2]
    return resistance + " " + tolerance
  else:
    digit = int(base[colors[0]][0] + base[colors[1]][0]+ base[colors[2]][0])
    magnitude = 10**int(base[colors[3]][1])
    resistance = res(digit * magnitude)
    tolerance = base[colors[4]][2]
    tcr = base[colors[5]][3]
    return resistance + " " + tolerance + " " + tcr
print (resistor_code(["black", "white", "black", "orange", "red", "yellow"]))

