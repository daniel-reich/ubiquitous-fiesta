
def fiscal_code(person):
  months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H","7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
  d, m, y = person['dob'].split('/')
​
  surname = get_name_code(person['surname'])
  name = get_name_code(person['name'],False)
  gender = get_gender_code(d,person['gender'])
  year = y[-2:]
  month = months[m]
  
  return ''.join([surname, name, year, month, gender])
​
def get_name_code(name,surname=True):
  c = ''.join(ch for ch in name.upper() if ch not in 'AEIOU')
  if not surname and len(c) > 3:
    c = c[0]+c[2:4]
  v = ''.join(ch for ch in name.upper() if ch in 'AEIOU')
  cv = c+v
  if len(cv) < 3:
    x = 'X' * (3 - len(cv))
    return c + v + x
  else:
    return cv[:3]
​
def get_gender_code(date,gender):
  if gender == 'M':
    if len(date) == 1:
      date = '0'+date
    return date
  else:
    return str(int(date)+40)

