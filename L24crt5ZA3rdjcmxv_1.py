
months = { "01": "A", "02": "B", "03": "C", "04": "D", "05": "E", "06": "H",
"07": "L", "08": "M", "09": "P", "10": "R", "11": "S", "12": "T" }
attributes =  ['name', 'surname', 'gender', 'dob']
​
def code(word, skip2=False):
    consonants = ''.join(c for c in word.upper() if c not in 'AEIOU')
    vowels = ''.join(c for c in word.upper() if c in 'AEIOU')
    if skip2 and len(consonants) > 3:
        consonants = consonants[:1] + consonants[2:]
    return (consonants + vowels + 'XXX')[:3]
​
def fiscal_code(person):
    name, surname, gender, dob = map(person.get, attributes)
    day, month, year = [('0'+num)[-2:] for num in dob.split('/')]
    day = day if gender == 'M' else str(int(day) +40)
    return code(surname) + code(name, True) + year + months[month] + day

