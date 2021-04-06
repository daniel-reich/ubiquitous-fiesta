
def isbn13(txt):
    def isbn10_check(txt):
        sum = 0
        for i in range(9):
            sum += (10-i)*int(txt[i])
        if txt[9] == 'X':
            sum += 10
        else:
            sum += int(txt[9])
        if sum%11:
            return False
        return True
    
    def isbn13_check(txt):
        mult = [1,3,1,3,1,3,1,3,1,3,1,3,1]
        sum = 0
        for i in range(13):
            sum += mult[i]*int(txt[i])
        if sum%10:
            return False
        return True
​
    if not txt[:-1].isnumeric():
        return "Invalid"
    else:
        if not txt[9].isdigit() and txt[9] != "X":
            return "Invalid"
    
    if len(txt) == 10:
        if isbn10_check(txt):
            c = "978"+txt
            if c[-1] == 'X':
                for i in range(9):
                    if isbn13_check(c[:-1]+str(i)):
                        return c[:-1]+str(i)
            else:
                for i in range(9):
                    if isbn13_check(c[:-1]+str(i)):
                        return c[:-1]+str(i)
        else:
            return "Invalid"
    if len(txt) == 13:
        if isbn13_check(txt):
            return "Valid"
    return "Invalid"

