
import re
def find_pattern(dict_, p):
    new = []
    for i in dict_:
        pattern = re.compile("[{0}|{1}]{2}".format(p[0].lower(), p[0].upper(), p[1:]))
        result = pattern.findall(string=dict_[i])
​
        if result: new += ['{0} = {1}'.format(i, result[0])]
        else: new += ['{0} = {1}'.format(i, "None")]
​
    return sorted(new)

