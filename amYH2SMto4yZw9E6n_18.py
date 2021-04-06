
import re
​
def validate(s):
    result = [re.match('[\+]?[1]?[ ./-]?[\(]?892[)|-]?[ ]?445-7663',s) or re.match('[1]?[./ ]?892[./ ]?567[./ ]?8901',s)]
    return not None in result

