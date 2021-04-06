
import string
​
def is_autobiographical(n):
    str_num = str(n)
    if len(str_num) > 10:
        return False
    for i in range(len(str_num)):
        if str_num.count(str(i)) != int(str_num[i]):
            return False
    return True

