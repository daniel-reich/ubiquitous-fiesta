
import re
def to_camel_case(string):
    string = re.split('[- _]', string)
    return "".join([string[i].capitalize() if i !=0 else string[i] for i in range(len(string))])

