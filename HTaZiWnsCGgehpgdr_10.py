
def license_plate(s, n):
    res=''
    s=s.replace('-','').upper()[::-1]
    a=[s[i:i+n]for i in range(0,len(s),n)]
    for i  in a[::-1]:
        res+=i[::-1]+'-'
    return res[0:-1]

