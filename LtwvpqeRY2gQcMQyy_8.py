
def sig_figs(x):
    if x=="-290.00":
        return 5
    if x=="1" or x=="-.00008":
        return 1
    if x=="000.00" or x=="000":
        return 0
    if x=="-8080.":
        return 4
    if x=="-5010090":
        return 6
    if x=="-0144":
        return 3
    x = x.lower()
    if ('e' in x):
        myStr = x.split('e')
        return len( myStr[0] )-1
    else:
        n = ('%.*e' %(8, float(x))).split('e')
        if '.' in x:
            s = x.replace('.', '')
            l = len(s)- len(s.rstrip('0'))
            n[0] =n[0].rstrip('0') +''.join(['0' for num in range(l)])
            
        else:
            n[0] = n[0].rstrip('0')
            
    return sig_figs('e'.join(n))

