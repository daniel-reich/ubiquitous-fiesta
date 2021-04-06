
import re
​
​
def fiscal_code(obj):
  months = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
            "7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T"}
​
  surVowels = [c.lower() in ('a', 'e', 'i', 'o', 'u') for c in obj['surname']]
  vowels = [c.lower() in ('a', 'e', 'i', 'o', 'u') for c in obj['name']]
  surnameCode = ''.join([c.upper() if surVowels[i] is False else '' for i,
                         c in enumerate(obj['surname'])] + [obj['surname'][j].upper() for j in [i for i, x in enumerate(surVowels) if x is True]])
  surnameCode = surnameCode + 'X'*(3-len(surnameCode)) if len(surnameCode) < 3 else surnameCode[:3]
  nameCode = ''.join([obj['name'][j].upper() for j in [i for i, x in enumerate(vowels) if x is False]])
  if len(nameCode) < 3:
    nameCode = str(nameCode + obj['name'][vowels.index(True)].upper() + 'X')[:3]
  elif len(nameCode) > 3:
    nameCode = ''.join([nameCode[i] for i in (0, 2, 3)])
  monthCode = months[re.compile(r'/(\d+)/').search(obj['dob']).group(1)]
  dayCode = re.compile(r'(\d+)/').search(obj['dob']).group(1)
  dayCode = '0' + dayCode if int(dayCode) < 10 else dayCode
  dayCode = str(int(dayCode) + 40) if obj['gender'] is 'F' else dayCode
  return surnameCode + nameCode + obj['dob'][-2:] + monthCode + dayCode

