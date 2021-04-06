
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
  res = "".join([c for c in person["surname"].upper() if c not in ['A', 'U', 'O', 'I', 'E']])[:3]
  if len(res) < 3:
    res = (res + "".join([c for c in person["surname"].upper() if c in ['A', 'U', 'O', 'I', 'E']]))[:3]
  if len(res) < 3:
    res += "X" * (3 - len(res))
  res += "".join([c for c in person["name"].upper() if c not in ['A', 'U', 'O', 'I', 'E']])[:4]
  if len(res) > 6:
    res = res[:4] + res[5:]
  elif len(res) < 6:
    res = (res + "".join([c for c in person["name"].upper() if c in ['A', 'U', 'O', 'I', 'E']]))[:6]
  if len(res) < 6:
    res += "X" * (6 - len(res))
  res += person["dob"].split('/')[2][-2:] + months[person["dob"].split('/')[1]]
  if person["gender"] == "M":
    res += person["dob"].split('/')[0].zfill(2)
  else:
    res += str(int(person["dob"].split('/')[0]) + 40)
  return res

