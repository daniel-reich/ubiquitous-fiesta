
import re
​
def lambda_to_def(code):
    pattern = r"(\w+) ?= ?lambda (.+): (.*)"
    temp = re.compile(pattern)
    matches = temp.findall(code)
    return "def {}({}):\n\treturn {}".format(matches[0][0],matches[0][1],
                                             matches[0][2])

