
def lychrel(num):
    i = 0
    while i < 500:
        num2 = str(num)[::-1]
        if str(num) == num2:
            return i
            break
        else:
            s = int(num) + int(num2)
            if str(s) == str(s)[::-1]:
                i+=1
                return i
                break
            else:
                num = s
                i+=1
                continue
    else:
        return True

