
def pyramidal_string(string, _type):
    v = []
    for i in range(1,50):
        v.append(int(.5*i*(i+1)))
    if len(string) == 0:
        return []
    if len(string) not in v:
        return 'Error!'
    if len(string) == 1:
        return [string]
    m = []
    if _type == 'REG':
        a = 1
        b = 0
        while b < len(string):
            temp = ''
            for i in range(a):
                temp += string[b]+' '
                b += 1
            m.append(temp[:-1])
            a += 1
        return m
    else:
        a = v.index(len(string))+1
        b = 0
        while b < len(string):
            temp = ''
            for i in range(a):
                temp += string[b]+' '
                b += 1
            m.append(temp[:-1])
            a -= 1
        return m

