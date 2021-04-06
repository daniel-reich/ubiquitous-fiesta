
def truncatable(n):
    l = True
    r = True
​
    for i in range(2, n):
        if n % i == 0:
            return False
    if str(n).count("0") == 0:
        for x in range(1, len(str(n))):
            asd1 = int(str(n)[x:])
            if int(str(n)[x:]) < 2: l = False
            for y in range(2, int(str(n)[x:])):
                if int(str(n)[x:]) % y == 0:
                    l = False
​
        for x in range(1, len(str(n))):
            asd2 = int(str(n)[:-x])
            if int(str(n)[:-x]) < 2: r = False
            for y in range(2, int(str(n)[:-x])):
                if int(str(n)[:-x]) % y == 0:
                    r = False
    else:
        return False
    if l == True and r == True:
        return "both"
    elif l == True and r == False:
        return "left"
    elif l == False and r == True:
        return "right"
    elif l == False and r == False:
        return False

