
import re
def seven_boom(lst):
    for i in lst:
        if re.search("7",str(i)):
            return "Boom!"
    return "there is no 7 in the list"

