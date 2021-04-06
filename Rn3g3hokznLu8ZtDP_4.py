
def increment_string(txt):
    if not txt[-1].isdigit(): return txt + '1'
    else:
        num = [x for x in txt if x.isdigit()]
        let = ''.join(x for x in txt if x.isalpha())
        a=list(str(int(''.join(num))+1)[::-1])+['0']*(len(num)-len(str(int(''.join(num))+1)))
        return let + ''.join(a[::-1])

