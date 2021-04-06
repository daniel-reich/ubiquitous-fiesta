
import re
def replace_nums(string):
    string = re.sub(r'\d+',lambda x: bin(int(x.group()))[2:],string)
    return string

