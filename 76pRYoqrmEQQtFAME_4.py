
def is_astonishing(num):
    s = str(num)
    for i in range(1, len(s)):
        a = int(s[:i])
        b = int(s[i:])
        if a < b:
            if get_sum(a,b) == num:
                return"AB-Astonishing"
        else:
            if get_sum(b,a) == num:
                return "BA-Astonishing"
    return False
​
def get_sum(x,y):
    return x + (y*(y+1)//2 - x*(x+1)//2)

