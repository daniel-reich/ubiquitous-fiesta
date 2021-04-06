
from datetime import datetime
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
  result = ""
  snnotvow = ""
  snvow = ""
  
  for i in person["surname"].upper():
    if i in "AEIOU":
      snvow += i
    else:
      snnotvow += i
  snnotvow = snnotvow + snvow + "XXX" 
  result = snnotvow[:3]
  nnotvow = ""
  nvow = ""
  
  for i in person["name"].upper():
    if i in "AEIOU":
      nvow += i
    else:
      nnotvow += i
      
  if len(nnotvow) == 3:
    result += nnotvow
  elif len(nnotvow) > 3:
    result = result + nnotvow[0] + nnotvow[2] + nnotvow[3]
  else:
    nnotvow = nnotvow + nvow + "XXX"
    result += nnotvow[:3]
  
  date_object = datetime.strptime(person["dob"], '%d/%m/%Y').date()
  result += str(date_object.year)[2:]
  result += months[str(date_object.month)]
  
  if person["gender"] == "M":
    if date_object.day < 10:
      result += "0"
      result += str(date_object.day)
    else:
      result += str(date_object.day)
  else:
    result += str(date_object.day + 40)
  return result

