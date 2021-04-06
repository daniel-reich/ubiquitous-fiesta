
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
  code = ''
  surname_c = [i for i in person['surname'].upper() if i not in 'AEIOU']
  surname_v = [i for i in person['surname'].upper() if i in 'AEIOU']
  if len(person['surname']) <= 2:
    code += surname_c[0]+surname_v[0]+'X'
  elif len(surname_c) >= 3:
    code += ''.join(surname_c[:3])
  else:
    code += ''.join(surname_c)+surname_v[0]
  name_c = [i for i in person['name'].upper() if i not in 'AEIOU']
  name_v = [i for i in person['name'].upper() if i in 'AEIOU']
  if len(person['name']) <= 2:
    code += name_c[0]+name_v[0]+'X'
  elif len(name_c) == 3:
    code += ''.join(name_c)
  elif len(name_c) > 3:
    code += name_c[0]+name_c[2]+name_c[3]
  else:
    code += ''.join(name_c)+name_v[0]
  code += person['dob'][-2:]+months[person['dob'].split('/')[1]]
  if person['gender'] == 'M':
    if int(person['dob'].split('/')[0]) < 10:
      code += '0'+person['dob'].split('/')[0]
    else:
      code += person['dob'].split('/')[0]
  else:
    code += str(int(person['dob'].split('/')[0])+40)
  return code

