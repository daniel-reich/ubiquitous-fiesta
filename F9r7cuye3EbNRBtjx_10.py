
import re
​
def string_builder(s):
    pattern = "([1-9][0-9]*)\[(\w*)\]"
    substitute = lambda m: m.group(2)*(int(m.group(1)))
    result = s
    while True:
        new_result = re.sub(pattern, substitute, result)
        if new_result == result:
            break
        else:
            result = new_result
    return(result)

