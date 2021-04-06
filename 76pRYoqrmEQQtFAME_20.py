
def is_astonishing(num):
    txt = str(num)
​
    for i in range(1,len(txt)):
        a = int(txt[:i])
        b = int(txt[i:])
        if a < b:
            t = ((b-a+1)*(a+b))//2
​
            if t == num:
                return 'AB-Astonishing'
        else:
            t = ((a-b+1)*(a+b))//2
​
            if t == num:
                return 'BA-Astonishing'
    return False

