
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
vowels = {"A","E","I","O","U"}
​
def fiscal_code(person):
  fscode = []
  for c in person["surname"]:
        if c.upper() not in vowels:
          fscode.append(c.upper())
          if len(fscode) == 3:
            break
  if len(fscode) < 3:
    for c in person["surname"]:
      if c.upper() in vowels:
        fscode.append(c.upper())
        if len(fscode) == 3:
          break
  while len(fscode) < 3:
    fscode.append("X")
    
  cons = []
  for c in person["name"]:
    if c.upper() not in vowels:
      cons.append(c.upper())
  if len(cons) > 3:
    fscode.extend([cons[0],cons[2],cons[3]])
  else:
    fscode.extend(cons)
  if len(fscode) < 6:
    for c in person["name"]:
      if c.upper() in vowels:
        fscode.append(c.upper())
        if len(fscode) == 6:
          break 
  while len(fscode) < 6:
    fscode.append("X")
    
  dob = person["dob"].split("/")
  fscode.extend(dob[2][2:])
  fscode.append(months[dob[1]])
  last = int(dob[0])
  if person["gender"] == "F":
    last += 40
  if last < 10:
    fscode.extend(["0",str(last)])
  else:
    fscode.extend(str(last))
    
  return "".join(fscode)

