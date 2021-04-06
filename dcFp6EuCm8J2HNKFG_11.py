
import re 
def func(l):
    return len(re.findall('[0-9A-Za-z]',str(l)))+(str(l).count('[')-1)

