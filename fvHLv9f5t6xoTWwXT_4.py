
import re
def grab_number_sum(s):
    P = re.compile(r"\d+")
    X = re.findall(P,s)
    return sum(map(int,X))

