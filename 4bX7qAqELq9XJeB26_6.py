
import re
def to_camel_case(x):
    for i in range(len(x)):
        if x[i]=="_" or x[i]=="-":
            x = x.replace(x[i+1],x[i+1].upper())
    return re.sub(r'[_-]','',x)

