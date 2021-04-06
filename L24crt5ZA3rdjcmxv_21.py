
import re
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
  sn = person["surname"].upper()
  n = person["name"].upper()
  g = person["gender"].upper()
  d = person["dob"].split("/")
  res = ""
  
  sn_con = "".join(re.findall(r'[^AEIOU]', sn))
  sn_vow = "".join(re.findall(r'[AEIOU]', sn))
  
  n_con = "".join(re.findall(r'[^AEIOU]', n))
  n_vow = "".join(re.findall(r'[AEIOU]', n))
  
  if len(sn_con) >= 3:
    res += sn_con[:3]
  elif len(sn) >= 2 and len(sn_vow) > 1:
    res += sn_con + sn_vow[0]
  else:
    res += sn_con + sn_vow + ("X" * (3 - len(sn)))
  
  if len(n_con) == 3:
    res += n_con
  elif len(n_con) > 3:
    res += n_con[0] + n_con[2] + n_con[3]
  elif len(n_con) >= 2:
    res += n_con + n_vow[0]
  else:
    res += n_con + n_vow + ("X" * (3 - len(n)))
  
  res += d[2][-2:] + months[d[1]]
  if g == "M":
    if int(d[0]) < 10:
      res += "0" + d[0]
    else:
      res += d[0]
  else:
    res += str(int(d[0]) + 40)
  
  return res

