
import re
def replace_nums(string):
    return re.sub(r'(\d+)',lambda x:bin(int(x.group()))[2:],string)

