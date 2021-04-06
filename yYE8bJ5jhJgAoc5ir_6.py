
def bugger(num):
    c = 0
    while len(str(num))>1:
        num = eval("*".join([i for i in str(num)]))
        c+=1
    return c

