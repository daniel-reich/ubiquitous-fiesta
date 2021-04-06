
def valid_name(s):
    if len(s.split())==3:
        a,b,c=s.split()
        if (len(a) == 2 and len(b)==2 and a.find('.')==1 and b.find('.')==1)\
        or (len(a) > 2 and len(b)==2 and b.find('.')==1 and a[0].isupper())\
        or (len(a) > 2 and len(b) > 2 and b.find('.') !=1 and a.find('.') != 1)\
        and a[0].isupper() and b[0].isupper() and c[0].isupper() and len(c) > 1 and c.find('.') !=1 :
            return True
        else:
            return False
    elif len(s.split())==2:
        a,c=s.split()
        if a.find('.')==1 and a[0].isupper() and c[0].isupper() and len(c) > 2:
            return True
        else:
            return False
    else:
        return False

