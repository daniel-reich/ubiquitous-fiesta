
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
  res = ''
  vocal = ['A','E','I','O','U']
  for i in person['surname'].upper():
    if i not in vocal:
      res += i
  if len(res) < 3:
    for i in person['surname'].upper():
      if i in vocal and len(res)<3:
        res += i
  if len(res) < 3:
    for i in person['surname'].upper():
      if len(res)< 3:
        res += 'X'
  l = []
  for i in person['name'].upper():
    if i not in vocal:
      l.append(i)
  if len(l)<4:
    for i in person['name'].upper():
      if i not in vocal:
        res += i
    if len(res) < 6:
      for i in person['name'].upper():
        if i in vocal and len(res)<6:
          res += i
    if len(res) < 6:
      for i in person['name'].upper():
        if len(res)< 6:
          res += 'X'
  else:
    for i in range(4):
      if i != 1:
        res += l[i]
  d, m, y = person['dob'].split('/')
  res += str(y)[-2:]
  res += months[str(m)]
  if person['gender'] == 'F':
    d = int(d)
    d += 40 
    d = str(d)
  if len(d) == 1:
    d = '0'+d
  res += d
  return res

