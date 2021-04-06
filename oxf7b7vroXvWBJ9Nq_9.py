
def discount(n, txt):
    if txt:
        x = [i for i in txt.split(',') if i[-1]=='%'] + [i for i in txt.split(',') if i[-1]!='%']
        for i in x:
            if i[-1] == '%':
                n = n * (100-float(i.strip('%')))/100
            else:
                n = n - float(i)
    return round(n,2)

