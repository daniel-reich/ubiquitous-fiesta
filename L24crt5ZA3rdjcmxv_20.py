
def get_letters(s):
    return ''.join(sorted(s.upper(), key=lambda x: x in 'AEIOU') + ['X'])
​
def fiscal_code(person):
    months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H", 
               "7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
    
    part1 = get_letters(person['surname'])[:3]
    part2 = get_letters(person['name'])
​
    if len(part2) >= 4 and part2[3] not in 'AEIOU':
        part2 = ''.join((part2[0], part2[2], part2[3]))
    else:
        part2 = part2[:3]
​
    d, m, y = person['dob'].split('/')
    part3 = y[-2:]
    part4 = months[m]
    part5 = d.zfill(2) if person['gender'] == 'M' else str(int(d) + 40)
    
    return ''.join((part1, part2, part3, part4, part5))

