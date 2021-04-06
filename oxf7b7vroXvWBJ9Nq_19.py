
def discount(n, txt):
    if not txt:
        return n
    count=txt.split(',')
    count.reverse()
    for i in count:
        if '%' in i:
            n=(100-float(i.replace('%','')))/100*n
    for i in count:
        if '%' not in i:
            n=n-float(i)        
    return round(n,2)

