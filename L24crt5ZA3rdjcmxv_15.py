
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
  return surname(person["surname"].upper()) + firstname(person["name"].upper()) + date(person["dob"], person["gender"])
def surname(name):
  return ("".join(sorted(name, key = lambda l : l in "AEIOU")) + "XXX")[:3]
def firstname(name):
  letters = "".join(sorted(name, key = lambda l : l in "AEIOU"))
  return (letters + "XXX")[:3] if (len(letters) <= 3 or letters[3] in "AEIOU") else letters[0] + letters[2:4]
def date(dob, gender):
  return dob[-2:] + months[dob.split('/')[1]] + ("0" + str(int(dob.split('/')[0]) + (40 if gender == "F" else 0)))[-2:]

