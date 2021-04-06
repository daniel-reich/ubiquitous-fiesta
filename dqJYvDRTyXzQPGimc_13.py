
import re
​
​
def is_unfair_hurdle(hurdles):
    if len(hurdles) > 3:
        return True
    for hurdle in hurdles:
        unfair = re.findall(r"# {0,3}#", hurdle)
        if unfair:
            return True
    return False

