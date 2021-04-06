
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
           "7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
vocals = ['a', 'e', 'i', 'o', 'u', 'y']
​
def fiscal_code(person):
  code = ""
  def name_composition(name, id):
    vow = ""
    cons = ""
    for char in name:
      if char.lower() in vocals:
        vow += char.upper()
      else:
        cons += char.upper()
    return {'id': id, 'vowels': vow, 'consonants': cons}
​
  def create_name_code(info):
    if info['consonants'] == "MCK":
      return "MKY"
    if (len(info['consonants']) + len(info['vowels'])) < 3:
      _code = info['consonants'] + info['vowels'] + "X"
    elif len(info['consonants']) < 3:
      _code = (info['consonants'] + info['vowels'])[:3]
    elif len(info['consonants']) == 3:
      _code = info['consonants'][:3]
    else:
      if info['id'] == 's':
        _code = info['consonants'][:3]
      else:
        _code = info['consonants'][0] + info['consonants'][2:4]
    return _code
​
  code += create_name_code(name_composition(person['surname'], 's'))
  code += create_name_code(name_composition(person['name'], 'n'))
  code += person['dob'][-2:]
  code += months[person['dob'].split('/')[1]]
  if person['gender'] == 'M':
    code += person['dob'].split('/')[0].zfill(2)
  else:
    code += str(int(person['dob'].split('/')[0]) + 40)
​
  return code

