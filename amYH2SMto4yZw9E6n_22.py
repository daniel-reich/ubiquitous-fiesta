
def validate(s):
​
    if len(s) == 16:
        aux = s.split()
        if len(aux[0]) == 1 and len(aux[1]) == 5 and len(aux[-1]) == 8:
            return aux[1][0] == '(' and aux[1][-1] == ')' and aux[-1][3] == '-'
​
    elif len(s) == 15:
        aux = s.split('-')
        if len(aux[0]) == 2 and len(aux[1]) == len(aux[2]) and len(aux[-1]) == 4:
            return s[0] == '+' and s[2] == s[6] == s[10]
​
    elif len(s) == 14:
        if s[1] == s[5] == s[9]:
            return True
        return s[0] == '(' and s[4:6] == ') ' and s[9] == '-'
​
    elif len(s) == 12:
        return s[3] == s[7] and s[3] in [' ', '.', '/', '-']
​
    elif len(s) in [10, 11]:
        try:
            return bool(int(s))
        except:
            pass
    return False

