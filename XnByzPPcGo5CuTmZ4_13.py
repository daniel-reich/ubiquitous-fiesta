
def kix_code(addr):
    a=addr.split(',')
    for i in range(len(a)):
        a[i]=a[i].split()
    kix=a[2][0]+a[2][1]
    if a[1][-1].isalpha() and a[1][-2].isnumeric():
        kix+=a[1][-2]+'X'+a[1][-1].upper()
    else:
        for i in a[1][-1]:
            if not i.isalnum():
                a[1][-1]=a[1][-1].replace(i,'X')
                break
        kix+=a[1][-1].upper()    
    return kix

