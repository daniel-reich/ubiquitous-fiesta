
import re
def validate(s):
    if '  ' in s:
        return False
    x=re.split('[.+/)( -]',s)
    y=[i for i in x if i!='']
    if y[0].isnumeric() and y[0]==s:
        return True
    print(y)
    a=sum(len(i) for i in y)
    if y[0]=='1':
        y.pop(0)
        if a!=11:
            return False
    if len(y[0])!=3 or len(y[1])!=3 or len(y[2])!=4:
        return False
    if not ''.join(y).isnumeric():
        return False
    return True

