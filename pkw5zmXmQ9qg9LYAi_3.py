
import re
​
​
def space_message(txt):
    return space_message(re.sub(
        r"\[(\d)(\w+)\]", 
    lambda match: int(match.group(1)) * match.group(2), 
    txt
    )) if '[' in txt else txt

