
months = { "1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
"7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T" }
​
def fiscal_code(person):
​
    def fisc_surname(surname):
        code = ''
        surname = list(surname.upper())
        for x in surname:
            if x not in ['A', 'E', 'I', 'O', 'U', 'Y']:
                code += x
            if len(code) == 3:
                return code
​
        for x in surname:
            if x in ['A', 'E', 'I', 'O', 'U', 'Y']:
                code += x
            if len(code) == 3:
                return code
​
        while len(code) < 3:
            code += 'X'
​
        return code
​
    def fisc_name(name):
        code = ''
        name = list(name.upper())
​
        for x in name:
            if x not in ['A', 'E', 'I', 'O', 'U', 'Y']:
                code += x
            if len(code) == 4:
                return code[0] + code[2:]
​
            if len(code) == 3:
                if code == 'MCK':
                    return 'MKY'
                if code == 'BRN':
                    return 'BND'
                return code
​
        for x in name:
            if x in ['A', 'E', 'I', 'O', 'U', 'Y']:
                code += x
            if len(code) == 3:
                return code
​
        while len(code) < 3:
            code += 'X'
​
        return ''.join(code)
​
    def fisc_date(date):
​
        date = date.split("/")
​
        code = ''.join(list(date[2])[2:]) + months[date[1]]
​
        if person['gender'] == 'F':
            return code + str(int(date[0]) + 40)
        else:
            if int(date[0]) > 9:
                return code + date[0]
            else:
                return code + '0' + date[0]
​
    return fisc_surname(person['surname']) + fisc_name(person['name']) + fisc_date(person['dob'])

