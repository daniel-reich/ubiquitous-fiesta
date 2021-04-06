
def is_astonishing(num):
    t = str(num)
    for i in range(len(t)-1):
        a = t[:i+1]
        b = t[i+1:]
        sum=0
        a1 = int(a)
        b1 = int(b)
        if (a1 < b1):
            sum = ((b1-a1)*(b1+a1+1)/2) + a1 
            flag = 1
        else :
            sum = ((a1-b1)*(a1+b1+1)/2) + b1
            flag = 2
        if num == sum:
            if flag == 1:
                return "AB-Astonishing"
            elif flag == 2:
                return "BA-Astonishing"
    return False

