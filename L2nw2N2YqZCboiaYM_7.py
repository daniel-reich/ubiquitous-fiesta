
def repeated(s):
    for i in range(1,int(len(s)/2)+1):
        if set(s.split(s[0:i])) == {''}:
            return True 
    return False

