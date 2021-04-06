
def add_str_nums(num1, num2):
    n1 = [i for i in num1]
    n2 = [i for i in num2]
    c = 0
    if len(n1)!=0:
        for i in n1:
            if ord(i)<48 or ord(i)>57:
                c = 1
                break
            else:
                pass
    else:
        n1 = ["0"]
    
    if len(n2)!=0:
        for i in n1:
            if ord(i)<48 or ord(i)>57:
                c = 1
                break
            else:
                pass
    else:
        n2 = ["0"]
    if c!= 1: 
        return str(int("".join(n1)) + int("".join(n2)))
    else:
        return "-1"

