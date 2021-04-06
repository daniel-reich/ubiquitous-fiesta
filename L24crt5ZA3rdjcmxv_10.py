
import string
​
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
vowels = set('AEIOU')
consonants = set(string.ascii_uppercase) - vowels
​
​
def get_consonants_vowels(word):
    return ''.join(filter(lambda x: x in consonants, word.upper())), ''.join(filter(lambda x: x in vowels, word.upper()))
​
​
def handle_surname(surname):
    surname_c, surname_v = get_consonants_vowels(surname)
    
    code = surname_c[:3]
    
    if len(code) < 3:
        code += surname_v[:3 - len(code)]
    
    while len(code) < 3:
        code += 'X'
    
    return code
​
​
def handle_name(name):
    name_c, name_v = get_consonants_vowels(name)
    
    if len(name_c) > 3:
        return name_c[0] + name_c[2:4]
    elif len(name_c) == 3:
        return name_c
    elif len(name_c) < 3:
        code = name_c + name_v[:3 - len(name_c)]
        
        while len(code) < 3:
            code += 'X'
        
        return code
​
​
def handle_dob_gender(dob, gender):
    dob_lst = dob.split('/')
    code = dob_lst[2][-2:]
    code += months[dob_lst[1]]
    day = int(dob_lst[0]) if gender == 'M' else int(dob_lst[0]) + 40
    day = str(day) if day >= 10 else '0' + str(day)
    return code + day
    
​
def fiscal_code(person):
    code = handle_surname(person['surname'])
    code += handle_name(person['name'])
    code += handle_dob_gender(person['dob'], person['gender'])
    
    return code

