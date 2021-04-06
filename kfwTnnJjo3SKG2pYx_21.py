
# with regex
#import re
#def replace_nums(string):
#    return re.sub(r"(\d+)", lambda m: bin(int(m.group()))[2:],string)
​
​
​
# without regex
​
​
def replace_nums(string):
    n, result= "", ""
    for i in string:
        if i.isnumeric(): n += i
        else:
            if not n == "":
                result += bin(int(n))[2:]
                n = ""
            result += i
            
    if not n == "": result += bin(int(n))[2:]
    return result

