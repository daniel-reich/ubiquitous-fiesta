
def decrypt(st1):
    lst=[]
    i=0
    while i in range(len(st1)-2):
        if (st1[i+2]!='#'):
            if st1[i]!='#':
              lst.append(st1[i])
            i=i+1
        else:
            lst.append(st1[i:i+2])
            i=i+2
    ls=st1[-1]
    if ls!='#':
        for i in st1[-2:]:
          if i!='#':
            lst.append(i)
    return ("".join([chr(int(i)+96) for i in lst]))

