
import re
def find_vertex(x):
    a,b,c = re.findall(r'-?\d+',x)
    return  -int(b)//(2*int(a))

