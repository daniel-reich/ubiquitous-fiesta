
months = {"1": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "H",
          "7": "L", "8": "M", "9": "P", "10": "R", "11": "S", "12": "T"}
​
​
def fiscal_code(person):
    vowels=['a','e','i','o','u']
    sur_c=''
    for c in person['surname'].lower():
        if c not in vowels and len(sur_c)<3:
            sur_c += c
    if len(sur_c)<3:
        for c2 in person['surname'].lower():
            if c2 in vowels and len(sur_c)<3:
                sur_c += c2
    if len(sur_c)<3:
        sur_c+=((3-len(sur_c))*'x')
​
    name_c=''
    for d in person['name'].lower():
        if d not in vowels and len(name_c)<4:
            name_c+=d
    if len(name_c)==4:
        name_c=name_c[0]+name_c[2:]
    for d2 in person['name'].lower():
        if len(name_c)<3 and (d2 in vowels):
            name_c+=d2
    if len(name_c)<3:
        name_c+=(3-len(name_c))*'x'
​
​
​
​
    dob=person['dob']
    y=dob[-2:]
    d=dob[0:dob.index('/')]
    m=dob[dob.index('/')+1:dob.rfind('/')]
    if person['gender']=='M' and len(d)==1:
        d="0"+d
    elif person['gender']=='F':
        d=str(int(d)+40)
    dob_c=y+months[m]+d
    res=(sur_c+name_c+dob_c).upper()
    return res

