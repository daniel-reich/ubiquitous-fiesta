
from itertools import repeat
​
months = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
      "7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T"}
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
​
​
def get_consonants(text):
  return ''.join([i for i in text if i not in vowels])
​
​
def get_vowels(text):
  return ''.join([i for i in text if i in vowels])
​
​
def handle_surname(surname):
  cons = get_consonants(surname)
  cons_count = len(cons)
  vow = get_vowels(surname)
  result = ""
  if cons_count >= 3:
    result = cons[:3]
  else:
    result = cons + vow[:3 - cons_count]
  if len(surname) < 3:
    result = cons + vow + ''.join(repeat('X', 3 - len(surname)))
  return result.upper()
​
​
def handle_name(name):
  cons = get_consonants(name)
  cons_count = len(cons)
  vow = get_vowels(name)
  result = ""
  if cons_count == 3:
    result = cons
  elif cons_count > 3:
    result = cons[0] + cons[2] + cons[3]
  else:
    result = cons + vow[:3 - cons_count]
  if len(name) < 3:
    result = cons + vow + ''.join(repeat('X', 3 - len(name)))
  return result.upper()
​
​
def handle_dob(dob, gender):
  d, m, y = dob.split("/")
  result = y[-2:] + months[m]
  day_value = ""
  if gender == "M":
    day_value = d if int(d) > 9 else "0" + d
  else:
    day_value = str(int(d) + 40)
  result += day_value
  return result
​
​
​
def fiscal_code(person):
  result = handle_surname(person["surname"])
  result += handle_name(person["name"])
  result += handle_dob(person["dob"], person["gender"])
  return result

